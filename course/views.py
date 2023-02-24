from django.shortcuts import render, HttpResponse

# Create your views here.

def course_view(request):
    return HttpResponse("<h1>Hello Course</h1>")
