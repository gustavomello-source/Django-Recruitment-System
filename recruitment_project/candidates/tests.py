from django.test import TestCase
from django.urls import reverse
from datetime import date
from .models import Candidate
from django.contrib.auth.models import User

class CandidateModelTest(TestCase):
    def setUp(self):        
        self.candidate = Candidate.objects.create(
            full_name="Test User",
            email="testuser@example.com",
            phone="+00 123456789",
            date_of_birth=date(2000, 1, 1),
            # Professional Experience fields
            company="Test Company",
            position="Software Developer",
            experience_start_date=date(2020, 1, 1),
            experience_end_date=date(2023, 1, 1),
            experience_description="Worked on various projects",
            # Academic Formation fields
            institution="Test University",
            degree="Bachelor's",
            field_of_study="Computer Science",
            education_start_date=date(2016, 1, 1),
            education_end_date=date(2020, 1, 1),
        )

    def test_candidate_creation(self):
        self.assertTrue(isinstance(self.candidate, Candidate))
        self.assertEqual(self.candidate.__str__(), "Test User")

    def test_candidate_fields(self):
        # Test basic information
        self.assertEqual(self.candidate.email, "testuser@example.com")
        self.assertEqual(self.candidate.phone, "+00 123456789")
        
        # Test professional experience
        self.assertEqual(self.candidate.company, "Test Company")
        self.assertEqual(self.candidate.position, "Software Developer")
        
        # Test academic formation
        self.assertEqual(self.candidate.institution, "Test University")
        self.assertEqual(self.candidate.degree, "Bachelor's")