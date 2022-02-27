from django.urls import path,include 
from django.urls.resolvers import URLPattern 

from .views import AboutView, HomeView, InfoView 

urlpatterns = [ 
    path('',HomeView.as_view(),name='home'),
    path('about',AboutView.as_view(),name='about'),
    path('info',InfoView.as_view(),name='info'),
]
