
from django.shortcuts import render
from .models import Course

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/list.html', {
        'courses': courses,
        'title': 'Available Courses'
    })

def course_detail(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, 'courses/detail.html', {
        'course': course,
        'title': course.title
    })
