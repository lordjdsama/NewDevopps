from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from . import models

class LessonListView(ListView):
  model = models.Lesson
  template_name = 'lessons/home.html'
  context_object_name = 'lessons'

# Create your views here.
def home(request):
  lessons = models.Lesson.objects.all()
  context = {
    'lessons': lessons
  }
  return render(request, 'lessons/home.html', context)

def about(request):
  return render(request, 'lessons/about.html', {'title': 'about page'})


class LessonDetailView(DetailView):
  model = models.Lesson

class LessonDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = models.Lesson
  success_url = reverse_lazy('lessons-home')

  def test_func(self):
    lesson = self.get_object()
    return self.request.user == lesson.author

class LessonCreateView(LoginRequiredMixin, CreateView):
  model = models.Lesson
  fields = ['title', 'description']

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

class LessonUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = models.Lesson
  fields = ['title', 'description']

  def test_func(self):
    lesson = self.get_object()
    return self.request.user == lesson.author

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)


# from django.shortcuts import render, HttpResponse
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.urls import reverse_lazy
# from . import models

# # Create your views here.
# def home(request):
#     lesson = models.Lesson.objects.all()
#     context = {
#         'lessons' : lesson
#     }
#     return render(request, "lessons/home.html", context)
    
# class LessonListView(ListView):
#     model = models.Lesson
#     template_name = 'lessons/home.html'
#     context_object_name = 'lessons'
    
# class LessonDetailView(DetailView):
#     model = models.Lesson 
    
# class LessonCreateView(LoginRequiredMixin, CreateView):
#     model = models.Lesson
#     fields = ['title', 'description']
    
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
        
# class LessonUpdateView(LoginRequiredMixin, UpdateView):
#     model = models.Lesson
#     fields = ['title', 'description']
    
#     def testfunc(self):
#         lesson = self.get_object()
#         return self.request.user == lesson.author
    
    
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
        
# class LessonDeleteView(LoginRequiredMixin, DeleteView):
#     model = models.Lesson
#     success_url = reverse_lazy('lessons-home')
    
#     def testfunc(self):
#         lesson = self.get_object()
#         return self.request.user == lesson.author

# def about(request):
#     return render(request, "lessons/about.html", {'title': 'about us page'})
        
# def about(request):
#     return render(request, "lessons/about.html", {'title': 'about us page'})
    
