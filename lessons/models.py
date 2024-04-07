from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Lesson(models.Model):
    """
    Model representing a lesson.
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
        """
        Return the absolute URL to access a detail record for this lesson.
        """
        return reverse("lessons-detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return str(self.title)
