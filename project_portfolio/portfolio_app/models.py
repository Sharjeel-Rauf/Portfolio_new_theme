from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class ProjectModel(models.Model):
    # Image associated with the project
    image = models.ImageField(upload_to='portfolio_app/media/')
    
    # Title of the project
    title = models.CharField(max_length=255)
    
    # Short name (1-5 words) for the project
    short_name = models.CharField(max_length=50)
    
    # Automatically created slug based on the title
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    # Created at field
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Automatically create a slug from the title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    # Define a string representation of the model
    def __str__(self):
        return self.title

    # Define a method to delete files when a project is deleted
    def delete(self, *args, **kwargs):
        # Delete the associated image
        if self.image:
            self.image.delete(save=False)
        # Delete associated details (i.e., ProjectDetailModel instances)
        self.details.all().delete()
        super().delete(*args, **kwargs)

class ProjectDetailModel(models.Model):
    # Reference to the related ProjectModel
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE, related_name='details')
    
    # Title of the code
    code_title = models.CharField(max_length=255)
    
    # Description of the code
    description = models.TextField()
    
    # Python file associated with the project
    python_file = models.FileField(upload_to='projects/files/', blank=True, null=True)

    # Define a string representation of the model
    def __str__(self):
        return self.code_title

    # Define a method to delete files when a project is deleted
    def delete(self, *args, **kwargs):
        # Delete the associated Python file
        if self.python_file:
            self.python_file.delete(save=False)
        super().delete(*args, **kwargs)

    def get_python_file_content(self):
        # Check if there is a Python file
        if self.python_file:
            # Open the file and read its content
            with self.python_file.open('r') as file:
                content = file.read()
            return content
        return None
    
class UserProfile(models.Model):
    description = models.TextField()
    email = models.EmailField()
    linkedin_url = models.URLField(max_length=200, blank=True, null=True)  # LinkedIn URL field
    
    def __str__(self):
        return self.email
    
class Summary(models.Model):
    summary = models.CharField(max_length=255, default="")

class ProfileDescription(models.Model):
    # Field for the top paragraph
    top_paragraph = models.TextField(blank=True, null=True, help_text='Enter the top paragraph of your profile description.')
    
    # Fields for other three paragraphs
    paragraph_1 = models.TextField(blank=True, null=True, help_text='Enter the first paragraph.')
    paragraph_2 = models.TextField(blank=True, null=True, help_text='Enter the second paragraph.')
    paragraph_3 = models.TextField(blank=True, null=True, help_text='Enter the third paragraph.')
    image = models.ImageField(blank=True, null=True, upload_to='portfolio_app/media/')
    
    def __str__(self):
        return f"Profile Description: {self.id}"
    
class WorkExperience(models.Model):
    job_title = models.CharField(max_length=100, help_text='Job title.', blank=True, null=True)
    company = models.CharField(max_length=100, help_text='Company name.', blank=True, null=True)
    start_year = models.IntegerField(help_text='Start year of the work period.', blank=True, null=True)
    end_year = models.IntegerField(help_text='End year of the work period. Use the current year if still working.', blank=True, null=True)

    def __str__(self):
        return f"{self.job_title} at {self.company}"
    
class Education(models.Model):
    title = models.CharField(max_length=100, help_text='Degree or certification title.')
    degree_institution = models.CharField(max_length=100, help_text='Name of the degree and institution.')
    start_year = models.IntegerField(help_text='Start year of the education period.')
    end_year = models.IntegerField(help_text='End year of the education period.')

    def __str__(self):
        return f"{self.title} at {self.degree_institution}"
    
class Discipline(models.Model):
    name = models.CharField(max_length=100, help_text='Discipline name.')

    def __str__(self):
        return self.name
    