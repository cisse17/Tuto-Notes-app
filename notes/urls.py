from django.urls import path
from .views import HomeView, NotesView, CreateNoteView, UpdateNoteView, DeleteNoteView, DetailNoteView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("notes/", NotesView.as_view(), name="notes"),
    path("creer/", CreateNoteView.as_view(), name="creer"),
    path("modifier/<str:pk>/", UpdateNoteView.as_view(), name="modifier"),
    path("supprimer/<str:pk>/", DeleteNoteView.as_view(), name="supprimer"),
    path("detail/<str:pk>/", DetailNoteView.as_view(), name="detail"),
    
]
