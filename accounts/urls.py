from django.contrib import admin
from django.urls import path

from .views import RegisterNoteView, LoginNoteView, LogoutNoteView

urlpatterns = [
    path("register/", RegisterNoteView.as_view(), name="register"),
    path("login/", LoginNoteView.as_view(), name="login"),
    path("logout/", LogoutNoteView.as_view(), name="logout"),

]