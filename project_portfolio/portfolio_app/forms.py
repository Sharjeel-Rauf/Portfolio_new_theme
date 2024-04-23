# forms.py
from django import forms
from .models import *
from django.core.exceptions import ValidationError



class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectModel
        fields = ['title', 'short_name', 'image']

class ProjectDetailForm(forms.ModelForm):
    MAX_CODE_TITLE_LENGTH = 255  # Define the maximum length for the code title
    
    class Meta:
        model = ProjectDetailModel
        fields = ['code_title', 'description', 'python_file']
    
    def clean_code_title(self):
        code_title = self.cleaned_data.get('code_title')
        if len(code_title) > self.MAX_CODE_TITLE_LENGTH:
            raise ValidationError(
                f'Code Title must be {self.MAX_CODE_TITLE_LENGTH} characters or less.'
            )
        return code_title

    def clean_python_file(self):
        python_file = self.cleaned_data.get('python_file')
        if python_file:
            # Get the file extension
            file_extension = python_file.name.split('.')[-1]
            # Check if the file extension is not 'py'
            if file_extension.lower() != 'py':
                raise ValidationError("Only Python files with .py extension are allowed.")
        return python_file
    
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['description', 'email']

class SummaryForm(forms.ModelForm):
    class Meta:
        model = Summary
        fields = ['summary']

class ProfileDescriptionForm(forms.ModelForm):
    class Meta:
        model = ProfileDescription
        fields = ['top_paragraph', 'paragraph_1', 'paragraph_2', 'paragraph_3', 'image']
        labels = {
            'top_paragraph': 'Top Paragraph',
            'paragraph_1': 'Paragraph 1',
            'paragraph_2': 'Paragraph 2',
            'paragraph_3': 'Paragraph 3',
            'image': 'Image',
        }
        help_texts = {
            'top_paragraph': 'Enter the top paragraph of your profile description.',
            'paragraph_1': 'Enter the first paragraph.',
            'paragraph_2': 'Enter the second paragraph.',
            'paragraph_3': 'Enter the third paragraph.',
            'image': 'Upload an image for your profile.',
        }


class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['job_title', 'company', 'start_year', 'end_year']