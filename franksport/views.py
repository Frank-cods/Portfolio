from django.shortcuts import render, redirect
from .models import Feedback
from .forms import FeedbackForm

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_success')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})

def feedback_success(request):
    feedback_entries = Feedback.objects.all().order_by('-date_submitted')
    return render(request, 'feedback_success.html', {'feedback_entries': feedback_entries})


def home(request):
    # Define variables for the home page content
    name = "Frank Ssekanjako"
    expertise = "Front-End and Back-End Django Web and Application Web Developer"

    # List of portfolio projects (replace with your actual project data)
    projects = [
        {
            'title': "Project 1 Title",
            'thumbnail': "project1-thumbnail.jpg",
            'description': "Brief description of Project 1.",
            'link': "/projects/project1",  # Replace with the actual project URL
        },
        {
            'title': "Project 2 Title",
            'thumbnail': "project2-thumbnail.jpg",
            'description': "Brief description of Project 2.",
            'link': "/projects/project2",  # Replace with the actual project URL
        },
        # Add more projects as needed
    ]

    # Render the home.html template with the data
    return render(request, 'home.html', {
        'name': name,
        'expertise': expertise,
        'projects': projects,
    })

def about_me(request):
    # You can define variables with your bio, education, skills, and other content here
    bio = "Hello! I'm Frank Ssekanjako, a passionate web developer..."
    education = "I hold a Bachelor's degree in Computer Science from XYZ University..."
    skills = ["HTML/CSS", "JavaScript", "Python", "Django", "React"]
    resume_link = "/media/resume.pdf"  # Update this with the actual path to your resume PDF

    # Contact information
    email = "frank@example.com"
    phone = "+1 (123) 456-7890"
    linkedin_profile = "https://www.linkedin.com/in/frank-ssekanjako"
    twitter_profile = "https://twitter.com/frankwebdev"

    # Testimonials
    testimonials = [
        {
            'quote': "Frank is an exceptional developer who consistently delivers high-quality work. His dedication to his craft and attention to detail are truly impressive.",
            'author': "John Doe, CEO of ABC Company"
        },
        # Add more testimonials as needed
    ]

    # Render the about_me.html template with the data
    return render(request, 'about_me.html', {
        'bio': bio,
        'education': education,
        'skills': skills,
        'resume_link': resume_link,
        'email': email,
        'phone': phone,
        'linkedin_profile': linkedin_profile,
        'twitter_profile': twitter_profile,
        'testimonials': testimonials,
    })
from .models import Feedback

def display_feedback(request):
    feedback_entries = Feedback.objects.all()
    return render(request, 'display_feedback.html', {'feedback_entries': feedback_entries})

from django.http import FileResponse
from django.conf import settings
import os

def movie(request):
    return render(request, 'movie.html')
