from django.shortcuts import render
from django.http import HttpResponse

#handles traffic from homepage of blog
def home(request):
	return HttpResponse('<h1>Blog Home Page</h1>')

def about(request):
	return HttpResponse('<h1>Blog About Page</h1>')