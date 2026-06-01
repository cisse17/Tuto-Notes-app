from django.shortcuts import render

from .forms import RegisterForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

class RegisterNoteView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, f"Bonjour {user.username} votre compte a été créé avec succés")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, "Erreur lors de l'inscription. Veuillez verifier les informations.")
        return super().form_invalid(form)
    

class LoginNoteView(LoginView):
    template_name = "accounts/login.html"

    def get_success_url(self):
        return reverse("home")

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        messages.success(self.request, f"Bon retour {username}")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, "Erreur veuillez verifier vos identifiants")
        return super().form_invalid(form)
    

class LogoutNoteView(LogoutView):
    next_page = reverse_lazy("login")

    def dispatch(self, request, *args, **kwargs):
        messages.success(self.request, "Vous avez été déconnecter avec succés. Merci et à bientôt.")
        return super().dispatch(request, *args, **kwargs)