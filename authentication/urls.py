from django.urls import path

from .views import *

urlpatterns = [
    path('api/registeraion/',Register.as_view()),
    path('api/login/',LoginView.as_view()),
    path('api/get/',UserView.as_view()),
    path('api/logout/',LogoutView.as_view()),

]
