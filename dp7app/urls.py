from django.urls import path
from dp7app import views

app_name="dp7app"

urlpatterns=[
    path('trial/',views.trial,name="trial"),
    path('profile/',views.profile,name="profile"),
]