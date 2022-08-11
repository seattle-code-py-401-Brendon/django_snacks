from django.urls import path
from .views import Homepageview, Aboutpageview

urlpatterns = [
    path('', Homepageview.as_view(), name='home'),
    path('about', Aboutpageview.as_view(), name='about'),
]
