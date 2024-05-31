from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('ourTeam/',views.ourTeam,name='ourTeam'),
    path('smartTrucks/',views.smartTrucks,name='smartTrucks'),
    path('solve/',views.solve,name='solve'),
]
