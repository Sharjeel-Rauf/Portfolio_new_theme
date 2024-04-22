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
    return redirect('title_page')


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



def portfolio_page_view(request):
    context = {}
    context['page_title'] = 'Portfolio Page'
    
    # Query all projects from the database
    projects = ProjectModel.objects.all()
    
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
            # If form is invalid, render the form with errors
            context = {
                'detail': detail,
                'form': form,
                'page_title': 'Edit Details',  # Page title for the response
            }
            # Return the response as a JSON object
            return JsonResponse({
                'html': render(request, 'portfolio_app/edit_project_details.html', context).content.decode('utf-8'),
                'page_title': context['page_title']
            })
    else:
        # Handle the GET request (render the edit form)
        form = ProjectDetailForm(instance=detail)
        context = {
            'detail': detail,
            'form': form,
            'page_title': 'Edit Details',  # Page title for the response
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
            # Add an error message if the form is invalid
            messages.error(request, "There was an issue with your submission. Please check the form and try again.")
    else:
        form = ProjectDetailForm()

    # Render the template with the form and project context
    return render(request, 'portfolio_app/add_project_detail.html', {'form': form, 'project': project, 'page_title': 'Add Project Detail'})


# view of the about page
def about_page_view(request):
    context = {}
    context['page_title'] = 'About Page'
    

    # Render the template with the context
    return render(request, 'portfolio_app/about.html', context)