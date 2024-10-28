from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from .models import Candidate
from datetime import date

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = [
            'full_name', 'email', 'phone', 'date_of_birth',
            'company', 'position', 'experience_start_date', 'experience_end_date', 'experience_description',
            'institution', 'degree', 'field_of_study', 'education_start_date', 'education_end_date',
            'resume'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control',}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: +1234567890'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'experience_start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'experience_end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'experience_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe your experience'}),
            'institution': forms.TextInput(attrs={'class': 'form-control'}),
            'degree': forms.TextInput(attrs={'class': 'form-control'}),
            'field_of_study': forms.TextInput(attrs={'class': 'form-control'}),
            'education_start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'education_end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'resume': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        experience_start = cleaned_data.get('experience_start_date')
        experience_end = cleaned_data.get('experience_end_date')
        education_start = cleaned_data.get('education_start_date')
        education_end = cleaned_data.get('education_end_date')

        if experience_start and experience_end and experience_start > experience_end:
            raise forms.ValidationError("Experience start date must be before end date")
        
        if education_start and education_end and education_start > education_end:
            raise forms.ValidationError("Education start date must be before end date")

        return cleaned_data
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Candidate.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("This email is already in use.")
        return email

class CandidateSearchForm(forms.Form):
    search = forms.CharField(required=False, label='Search by name or email')
    start_date = forms.DateField(required=False, label='Born after', widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(required=False, label='Born before', widget=forms.DateInput(attrs={'type': 'date'}))