"""
Module containing views for the lessons app.
"""
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from . import models

class LessonListView(ListView):
    """
    Module containing views for the lessons app.
    """
    model = models.Lesson
    template_name = 'lessons/home.html'
    context_object_name = 'lessons'

# Create your views here.
def home(request):
    """
    Module containing views for the lessons app.
    """
    lessons = models.Lesson.objects.all()# pylint: disable=no-member
    context = {
        'lessons': lessons
    }
    return render(request, 'lessons/home.html', context)

def about(request):
    """
    Module containing views for the lessons app.
    """
    return render(request, 'lessons/about.html', {'title': 'about page'})


class LessonDetailView(DetailView):
    """
    Module containing views for the lessons app.
    """
    model = models.Lesson

class LessonDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # pylint: disable=too-many-ancestors
    """
    Module containing views for the lessons app.
    """
    model = models.Lesson
    success_url = reverse_lazy('lessons-home')

    def test_func(self):
        lesson = self.get_object()
        return self.request.user == lesson.author

class LessonCreateView(CreateView): # pylint: disable=too-many-ancestors
    """
    View for creating a new lesson.
    """
    model = models.Lesson
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class LessonUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # pylint: disable=too-many-ancestors
    """
    Module containing views for the lessons app.
    """
    model = models.Lesson
    fields = ['title', 'description']

    def test_func(self):
        lesson = self.get_object()
        return self.request.user == lesson.author

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
