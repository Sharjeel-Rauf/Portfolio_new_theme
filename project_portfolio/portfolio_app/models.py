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
