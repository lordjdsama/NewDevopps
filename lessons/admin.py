"""
Admin configuration for lessons app.
"""

from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Lesson)
