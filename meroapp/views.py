#from django.shortcuts import render
#from django.http import HttpResponse
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"


#def Home_page_view(request):
    #return HttpResponse("Hello World! i somehow manage to understand the view.py and its link to the project urls")



# Create your views here.
