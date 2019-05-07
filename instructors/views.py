# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from instructors.models import Instructor

# Create your views here.


def hello(request):
        #print(dir(request))
        print(request.path)
        print(request.GET)
        print(request.POST)
        print(request.method)
	return render(request, "index.html")

def hello_python(request):
	return render(request, "python.html")

def sum_two(request, a, b):
    s = int(a) + int(b)
    print("Hi")
    return HttpResponse(s)

def indexblog(request):
        return HttpResponse("<h1>Blog</h1>")


def instructors_list(request):
	instructors = Instructor.objects.all()
	return render (request, "instructors.html", { "instructors_list": instructors })