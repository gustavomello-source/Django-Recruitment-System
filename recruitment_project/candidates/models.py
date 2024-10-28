from django.db import models
from django.urls import reverse

# I prefered to put all data inside a single class because of time constraints
# Had I more time to work on this project, I would have separated the class into more classes
# and used the ForeignKey field to link them together
class Candidate(models.Model):
    # General Information
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    
    # Professional Experience
    company = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=100, blank=True)
    experience_start_date = models.DateField(null=True, blank=True)
    experience_end_date = models.DateField(null=True, blank=True)
    experience_description = models.TextField(blank=True)
    
    # Academic Formation
    institution = models.CharField(max_length=100, blank=True)
    degree = models.CharField(max_length=100, blank=True)
    field_of_study = models.CharField(max_length=100, blank=True)
    education_start_date = models.DateField(null=True, blank=True)
    education_end_date = models.DateField(null=True, blank=True)
    
    resume = models.FileField(upload_to='resumes/', blank=True)
    
    class Meta:
        ordering = ['-id']
    
    def __str__(self):
        return f"{self.full_name}"
    
    def get_absolute_url(self):
        return reverse('candidate_detail', args=[str(self.id)])