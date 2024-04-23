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
    context = {}
    context['page_title'] = 'Create Project'

    # Handle POST request
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        
        
        if form.is_valid():
            # Validate the image
            image = form.cleaned_data.get('image')
            
            # Check if an image was uploaded
            if image:
                # Get image dimensions
                width, height = get_image_dimensions(image)
                
                # Validate image dimensions (e.g., check if width or height is zero)
                if width == 0 or height == 0:
                    messages.error(request, "Invalid image format. Please upload a valid JPEG or PNG image.")
                    return redirect('create_project')
                
                # Additional checks for image format can be added here
                
            else:
                messages.error(request, "No image uploaded.")
                return redirect('create_project')

            # If everything is valid, save the project instance
            project = form.save()
            # Display a success message including the project title
            messages.success(request, f'Project "{project.title}" created successfully!')
            # Redirect to the desired page (e.g., list of projects)
            return redirect('portfolio_page')
        else:
            # Display an error message if the form is invalid
            messages.error(request, 'There was an error creating the project.')

    else:
        # Handle GET request
        form = ProjectForm()

    # Pass the form to the template
    context['form'] = form
    
    return render(request, 'portfolio_app/create_project.html', context)

# view of the UPDATE project page
@login_required(login_url="portfolio_page")
def edit_project_view(request, project_id):
    # Get the project object using the provided project_id
    project = get_object_or_404(ProjectModel, id=project_id)
    print(project)

    if request.method == 'POST':
        # Create a form instance with the submitted data and files, and bind it to the project instance
        form = ProjectForm(request.POST, request.FILES, instance=project)

        if form.is_valid():
            # Validate the image
            image = form.cleaned_data.get('image')

            # Check if an image was uploaded
            if image:
                # Get image dimensions
                width, height = get_image_dimensions(image)
                
                # Validate image dimensions (e.g., check if width or height is zero)
                if width == 0 or height == 0:
                    messages.error(request, "Invalid image format. Please upload a valid JPEG or PNG image.")
                    return redirect('edit_project', project_id=project.id)
                
                # Additional checks for image format can be added here
                
            else:
                messages.error(request, "No image uploaded.")
                return redirect('edit_project', project_id=project.id)

            # If everything is valid, save the project instance
            form.save()
            # Display a success message
            messages.success(request, f'Project "{project.title}" updated successfully.')
            # Redirect to the project detail view
            return redirect('portfolio_page')
        else:
            # Display an error message if the form is invalid
            messages.error(request, "There was an error updating the project. Please check the form and try again.")

    else:
        # Create a form instance pre-filled with the existing project details
        form = ProjectForm(instance=project)

    # Render the edit project template with the form and project context
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


# view of the about page
def about_page_view(request):
    context = {}
    context['page_title'] = 'About Page'
    

    # Render the template with the context
    return render(request, 'portfolio_app/about.html', context)



@login_required(login_url="portfolio_page")
def add_summary(request):

    # Handle POST request
    if request.method == 'POST':
        form = SummaryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Summary added successfully.')
            return redirect('portfolio_page')
    else:
        form = SummaryForm()

    context = {'form': form}
    context['page_title'] = 'Add Summary'
    return render(request, 'portfolio_app/add_summary.html', context)

@login_required(login_url="portfolio_page")
def edit_summary(request):
    # Retrieve the current summary for the logged-in user
    summary = Summary.objects.first()

    # Handle POST request
    if request.method == 'POST':
        form = SummaryForm(request.POST, instance=summary)
        if form.is_valid():
            form.save()
            messages.success(request, 'Summary updated successfully.')
            return redirect('portfolio_page')
    else:
        # Initialize the form with the current summary instance
        form = SummaryForm(instance=summary)

    context = {'form': form}
    context['page_title'] = 'Edit Summary'
    # Use a different template for editing summary (e.g. edit_summary.html)
    return render(request, 'portfolio_app/edit_summary.html', context)






# view to add the user profile
@login_required(login_url="portfolio_page")
def add_user_profile(request):
    
    if request.method == 'POST':
        # Handle form submission
        form = UserProfileForm(request.POST)
        if form.is_valid(): 
            form.save()
            messages.success(request, 'Profile added successfully.')
            return redirect('portfolio_page')  # Redirect to the edit profile page
    else:
        # Handle GET request by providing a blank form
        form = UserProfileForm()
    
    # Render the form in the template
    context = {'form': form}
    context['page_title'] = 'Add User Profile'
    return render(request, 'portfolio_app/add_user_profile.html',  context)


# views to edit the profile
@login_required(login_url="portfolio_page")
def edit_user_profile(request):
    # Retrieve the current summary for the logged-in user
    user_profile = UserProfile.objects.first()

    if request.method == 'POST':
        # Handle form submission
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()  # Save the updated data
            messages.success(request, 'Profile updated successfully.')
            return redirect('portfolio_page')  # Redirect to the same page
    else:
        # Handle GET request
        form = UserProfileForm(instance=user_profile)
    
    # Render the form in the template
    context = {'form': form}
    context['page_title'] = 'Edit User Profile'
    return render(request, 'portfolio_app/edit_user_profile.html', context)