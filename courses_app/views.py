from django.shortcuts import render, redirect
from .models import Course
from django.contrib import messages

# Create your views here.

def index(request):
    context = {
        'all_courses': Course.objects.all()
    }
    return render(request, 'index.html', context)

def create(request):
    if request.method == "GET":
        return redirect('/')
    
    errors = Course.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect ('/')
        
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        Course.objects.create(name=name, description=description)
    return redirect('/')

def remove(request, id):
    if request.method == "GET":
        course = Course.objects.get(id=id)
        context = {
            "course": course
        }
        return render(request, 'remove.html', context)

    if request.method == "POST":
        course = Course.objects.get(id=id)
        course.delete()
    return redirect('/')
        


