from django.urls import path

#from .views import Home_page_view
from .views import HomePageView, AboutPageView

urlpatterns = [
    #path("", Home_page_view, name = "HOME"), # yo view ko function ko path ho
    path("", HomePageView.as_view(), name="home"), #yo view ko class ko path ho
    path("about/", AboutPageView.as_view(), name="about")
]