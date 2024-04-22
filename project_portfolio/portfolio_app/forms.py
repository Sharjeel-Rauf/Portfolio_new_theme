# forms.py
from django import forms
from .models import *
from django.core.exceptions import ValidationError



class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectModel
        fields = ['title', 'short_name', 'image']

class ProjectDetailForm(forms.ModelForm):
    class Meta:
        model = ProjectDetailModel
        fields = ['code_title', 'description', 'python_file']
    
    def clean_python_file(self):
        python_file = self.cleaned_data.get('python_file')
        if python_file:
            # Get the file extension
            file_extension = python_file.name.split('.')[-1]
            # Check if the file extension is not 'py'
            if file_extension.lower() != 'py':
                raise ValidationError("Only Python files with .py extension are allowed.")
        return python_file