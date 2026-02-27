
from django.shortcuts import render

from .models import Note
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from .forms import NoteForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin

# Create your views here.

class HomeView(TemplateView):
    template_name = "notes/home.html" 

class NotesView(ListView):
    model = Note
    template_name = "notes/notes.html"
    context_object_name = "notes"  
    
class CreateNoteView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = "notes/create.html"
    success_url = reverse_lazy("notes")


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_button"] = "Créer"
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "La note a été créée avec succés !")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Une erreur s'est produite lors de la création de la note.")
        return super().form_invalid(form)


class UpdateNoteView(UserPassesTestMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = "notes/create.html"
    success_url = reverse_lazy("notes")
    pk_url_kwarg = "id"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_button"] = "modifier"
        return context
    
    # return True or False
    def test_func(self):
        note = self.get_object()
        return  note.user == self.request.user
    
    def handle_no_permission(self):
        messages.error(self.request, "Vous n'avez pas la permission de modifier cette note.")
        return super().handle_no_permission()
    

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "La note a été modifiée avec succés !")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Une erreur s'est produite lors de la modification de la note.")
        return super().form_invalid(form)

  



