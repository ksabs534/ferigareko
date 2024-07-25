#from django.shortcuts import render
from django.http import HttpResponse

def Home_page_view(request):
    return HttpResponse("Hello World! i somehow manage to understand the view.py and its link to the project urls")

# Create your views here.
