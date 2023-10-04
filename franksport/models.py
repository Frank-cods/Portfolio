from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='project_thumbnails/')
    description = models.TextField()
    live_link = models.URLField()
    github_link = models.URLField()

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.author}: {self.quote}"

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.name}"