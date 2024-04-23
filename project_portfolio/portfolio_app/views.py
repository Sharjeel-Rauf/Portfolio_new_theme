from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions
from django.http import QueryDict
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse




# logout view
def logout_user(request):
    logout(request)
    return redirect('portfolio_page')


# view of the landing page
# Login
def title_page_view(request):
    context = {}
    context['page_title'] = 'Title Page'
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('portfolio_page')  # Redirect admin to admin portal
        else:
            return redirect('title_page')  # Redirect guest to guest portal

    next_url = request.GET.get('next')
    if next_url:
        request.session['next_url'] = next_url
    if request.method == "POST":
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        try:
            user_obj = User.objects.get(email = email)
        except:
            user_obj = None
        if user_obj:
            authenticated_user = authenticate(request, username=user_obj.username, password=password)
            if authenticated_user:
                login(request, authenticated_user)         
                print(user_obj)
                if user_obj.is_staff:
                    if 'next_url' in request.session:
                        del request.session['next_url']
                    # Authenticate admin user
                    return redirect('portfolio_page')  # Redirect admin to admin portal
            else:
                messages.error(request, "Invalid credentials. Please try again.")
                return redirect('title_page')
        else:
            messages.error(request, "Invalid credentials. Please try again.")
            return redirect('title_page')

    return render(request, 'portfolio_app/title_page.html', context)



# view for the main page
def portfolio_page_view(request):
    context = {}
    context['page_title'] = 'Portfolio Page'
    
    # Query all projects from the database and order them by the created_at field in descending order
    projects = ProjectModel.objects.all().order_by('-created_at')

    user_profile = UserProfile.objects.first()

    # Retrieve the summary for the logged-in user
    summary = Summary.objects.first()
    context['summary'] = summary

    context['summary'] = summary

    context['user_profile'] = user_profile
    
    # Add projects to the context
    context['projects'] = projects

    # Render the template with the context
    return render(request, 'portfolio_app/portfolio_page.html', context)

# view of the create project page
@login_required(login_url="portfolio_page")
def create_project_view(request):
    context = {'page_title': 'Create Project'}

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        
        if form.is_valid():
            # Validate the image
            image = form.cleaned_data.get('image')
            
            # Check if an image was uploaded
            if image:
                # Get image dimensions
                width, height = get_image_dimensions(image)
                
                # Validate image dimensions
                if width == 0 or height == 0:
                    form.add_error('image', "Invalid image format. Please upload a valid JPEG or PNG image.")
                else:
                    # If everything is valid, save the project instance
                    project = form.save()
                    messages.success(request, f'Project "{project.title}" created successfully!')
                    return redirect('portfolio_page')
            else:
                form.add_error('image', "No image uploaded.")
        
        # Display form errors
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(request, f"{field}: {error}")

    else:
        # Handle GET request
        form = ProjectForm()

    context['form'] = form
    return render(request, 'portfolio_app/create_project.html', context)

# view of the UPDATE project page
@login_required(login_url="portfolio_page")
def edit_project_view(request, project_id):
    project = get_object_or_404(ProjectModel, id=project_id)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)

        if form.is_valid():
            # Validate the image
            image = form.cleaned_data.get('image')
            
            # Check if an image was uploaded
            if image:
                # Get image dimensions
                width, height = get_image_dimensions(image)
                
                # Validate image dimensions
                if width == 0 or height == 0:
                    form.add_error('image', "Invalid image format. Please upload a valid JPEG or PNG image.")
                else:
                    # If everything is valid, save the project instance
                    form.save()
                    messages.success(request, f'Project "{project.title}" updated successfully.')
                    return redirect('portfolio_page')
            else:
                form.add_error('image', "No image uploaded.")
        
        # Display form errors
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(request, f"{field}: {error}")

    else:
        # Handle GET request
        form = ProjectForm(instance=project)

    context = {
        'form': form,
        'project': project,
        'page_title': 'Edit Project'
    }
    return render(request, 'portfolio_app/edit_project.html', context)

# View for deleting a project
@login_required(login_url="portfolio_page")
def delete_project_view(request, project_id):
    # Get the project by ID, or return a 404 error if not found
    project = get_object_or_404(ProjectModel, pk=project_id)

    # Handle POST request
    if request.method == 'POST':
        try:
            # Attempt to delete the project
            project.delete()
            
            # Display a success message
            messages.success(request, f'Project "{project.title}" deleted successfully!')
            
            # Redirect to the portfolio page
            return redirect('portfolio_page')
        except PermissionError as e:
            # Handle PermissionError
            messages.error(request, f'Error deleting project: {str(e)}')
            return redirect('delete_project', project_id=project_id)
    
    # If request is GET, render the confirmation page
    context = {
        'project': project,
        'page_title': 'Confirm Project Deletion'
    }
    
    return render(request, 'portfolio_app/delete_project.html', context)

# view to get the project details
def project_detail_view(request, project_id):
    # Fetch the specific project using the project_id
    project = get_object_or_404(ProjectModel, id=project_id)

    # Fetch the project details associated with the project
    project_details = project.details.all()

    # Read the content of each Python file associated with the project details
    if project_details:
        for detail in project_details:
            if detail.python_file:
                try:
                    with open(detail.python_file.path, 'r') as file:
                        detail.python_file_content = file.read()
                except Exception as e:
                    print(f"Error reading Python file {detail.python_file}: {e}")

    context = {
        'project': project,
        'project_details': project_details,
        'no_details': len(project_details) == 0,
        'page_title': 'Project Detail',
    }
    
    return render(request, 'portfolio_app/project_detail.html', context)

# view to edit the project details
@login_required(login_url="portfolio_page")
def edit_details_view(request, detail_id):
    # Get the detail object using the provided detail_id
    detail = get_object_or_404(ProjectDetailModel, id=detail_id)

    if request.method == 'POST':
        # Use the POST request body
        data = request.POST
        # Create the form instance with the submitted data and files
        form = ProjectDetailForm(data, request.FILES, instance=detail)

        if form.is_valid():
            # Save the detail
            form.save()
            # Redirect to the project detail view
            return redirect('project_detail', project_id=detail.project.id)
        else:
            # Handle form errors
            for field, errors in form.errors.items():
                for error in errors:
                    # Add each error to messages
                    messages.error(request, error)
                    
            # If form is invalid, render the form with errors
            context = {
                'detail': detail,
                'form': form,
                'page_title': 'Edit Details',
            }
            return render(request, 'portfolio_app/edit_project_details.html', context)
    else:
        # Handle the GET request (render the edit form)
        form = ProjectDetailForm(instance=detail)
        context = {
            'detail': detail,
            'form': form,
            'page_title': 'Edit Details',
        }
        return render(request, 'portfolio_app/edit_project_details.html', context)
    


# view to add the project details
@login_required(login_url="portfolio_page")
def add_project_detail_view(request, project_id):
    context = {}
    context['page_title'] = 'Add Project Detail'
    # Fetch the specific project using the project_id
    project = get_object_or_404(ProjectModel, id=project_id)
    
    if request.method == 'POST':
        # Create a form instance with the submitted data and files
        form = ProjectDetailForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a new ProjectDetailModel instance
            project_detail = form.save(commit=False)
            
            # Associate the project detail with the specific project
            project_detail.project = project
            project_detail.save()
            
            # Add a success message
            messages.success(request, "Project detail has been successfully added!")
            
            # Redirect to the project detail page
            return redirect('project_detail', project_id=project.id)
        else:
            # Iterate over each form error
            for field, errors in form.errors.items():
                # Add a field-specific error message to Django messages
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
    else:
        form = ProjectDetailForm()

    # Render the template with the form and project context
    context['form'] = form
    context['project'] = project
    return render(request, 'portfolio_app/add_project_detail.html', context)


@login_required(login_url="portfolio_page")
def add_summary(request):
    if request.method == 'POST':
        form = SummaryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Summary added successfully.')
            return redirect('portfolio_page')
        else:
            # Form is invalid, display the errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = SummaryForm()

    context = {'form': form}
    context['page_title'] = 'Add Summary'
    return render(request, 'portfolio_app/add_summary.html', context)

@login_required(login_url="portfolio_page")
def edit_summary(request):
    # Retrieve the current summary for the logged-in user
    summary = Summary.objects.first()

    if request.method == 'POST':
        form = SummaryForm(request.POST, instance=summary)
        if form.is_valid():
            form.save()
            messages.success(request, 'Summary updated successfully.')
            return redirect('portfolio_page')
        else:
            # Form is invalid, display the errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        # Initialize the form with the current summary instance
        form = SummaryForm(instance=summary)

    context = {'form': form}
    context['page_title'] = 'Edit Summary'
    return render(request, 'portfolio_app/edit_summary.html', context)






# view to add the user profile
@login_required(login_url="portfolio_page")
def add_user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile added successfully.')
            return redirect('portfolio_page')
        else:
            # Display form errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserProfileForm()

    context = {'form': form}
    context['page_title'] = 'Add User Profile'
    return render(request, 'portfolio_app/add_user_profile.html', context)

@login_required(login_url="portfolio_page")
def edit_user_profile(request):
    user_profile = UserProfile.objects.first()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('portfolio_page')
        else:
            # Display form errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserProfileForm(instance=user_profile)

    context = {'form': form}
    context['page_title'] = 'Edit User Profile'
    return render(request, 'portfolio_app/edit_user_profile.html', context)



# view of the about page
def about_page_view(request):
    # Query the database for the first instance of ProfileDescription
    profile_description = ProfileDescription.objects.first()

    context = {}
    context['page_title'] = 'About Page'

    if profile_description:
        # If data exists, set the context with the data from the model
        context['top_paragraph'] = profile_description.top_paragraph
        context['paragraph_1'] = profile_description.paragraph_1
        context['paragraph_2'] = profile_description.paragraph_2
        context['paragraph_3'] = profile_description.paragraph_3
        # Add image to context if available
        context['image_url'] = profile_description.image.url if profile_description.image else None
    else:
        # If no data exists, provide a button or link to add data
        context['add_data_button'] = True
    
        # Query the database for the user's work experiences
    work_experiences = WorkExperience.objects.all()  # You can filter this to a specific user if needed
    
      # Query the database for the user's work experiences
    work_experiences = WorkExperience.objects.all()  # Filtering by current user

    # Add work experiences to context
    context['work_experiences'] = work_experiences
    
    # Render the template with the context
    return render(request, 'portfolio_app/about.html', context)

# view to edit the profile description
@login_required(login_url="portfolio_page")
def profile_description_edit_add(request):
    # Retrieve the first ProfileDescription instance
    profile_description = ProfileDescription.objects.first()

    if request.method == 'POST':
        # Create a form instance with the request data and files
        form = ProfileDescriptionForm(request.POST, request.FILES, instance=profile_description)
        
        # Check if the form is valid
        if form.is_valid():
            form.save()  # Save the form data
            messages.success(request, 'Profile description saved successfully.')
            return redirect('about_page')  # Redirect to the 'about_page_view' URL
        else:
            messages.error(request, 'Error saving profile description. Please check the form data.')
    else:
        # Create a form instance with the existing profile description instance
        form = ProfileDescriptionForm(instance=profile_description)

    # Render the template with the form
    context = {'form': form}
    context['page_title'] = 'Add/Edit Profile Description'
    return render(request, 'portfolio_app/add_edit_profile_description.html', context)

@login_required(login_url="portfolio_page")
def edit_work_experience_view(request, experience_id=None):
    # If an experience ID is provided, retrieve the existing WorkExperience instance
    if experience_id:
        work_experience = get_object_or_404(WorkExperience, id=experience_id)
    else:
        work_experience = None

    # Create a form instance for WorkExperience, pre-filled if an existing instance is provided
    form = WorkExperienceForm(request.POST or None, instance=work_experience)

    if request.method == 'POST':
        # Check if the form is valid
        if form.is_valid():
            # Save the form data as a WorkExperience instance
            work_experience = form.save(commit=False)
            # If the instance is new, set the user field
            if work_experience.pk is None:
                work_experience.user = request.user
            # Save the instance
            work_experience.save()
            
            # Display success message
            messages.success(request, 'Work experience updated successfully.')
            # Redirect to a success page (e.g., the about page)
            return redirect('about_page')
        else:
            # Display form errors
            for field, errors in form.errors.items():
                for error in errors:
                    # Display each field error using messages.error
                    messages.error(request, f"{field.capitalize()}: {error}")

    # Render the form if request.method is GET or if the form is invalid
    # Render the template with the form
    context = {'form': form}
    context['page_title'] = 'Edit Work Experience'
    return render(request, 'portfolio_app/edit_work_experience.html', context)

@login_required(login_url="portfolio_page")  # Ensure that only authenticated users can add work experience
def add_work_experience_view(request):
    # Create a form instance for WorkExperience, pre-filled if an existing instance is provided
    form = WorkExperienceForm(request.POST or None)

    if request.method == 'POST':
        # Check if the form is valid
        if form.is_valid():
            # Save the form data as a WorkExperience instance
            work_experience = form.save(commit=False)
            # Optionally, set additional fields on the instance (e.g., user)
            work_experience.user = request.user
            work_experience.save()
            
            # Redirect to a success page (e.g., the about page)
            messages.success(request, 'Work experience added successfully.')
            return redirect('about_page')
        else:
            # Display form errors
            for field, errors in form.errors.items():
                for error in errors:
                    # Display each field error using messages.error
                    messages.error(request, f"{field.capitalize()}: {error}")

    # Render the form if request.method is GET or if the form is invalid
    # Render the template with the form
    context = {'form': form}
    context['page_title'] = 'Add Work Experience'
    return render(request, 'portfolio_app/add_work_experience.html', context)