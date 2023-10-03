from django.urls import path

from .views import *

urlpatterns = [
    path('api/user/registeraion/',Register.as_view()),
    path('api/user/login/',LoginView.as_view()),
    path('api/user/get/',UserView.as_view()),
    path('api/user/logout/',LogoutView.as_view()),

]
