from django.urls import path
from .views import HomeView, NotesView, CreateNoteView, UpdateNoteView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("notes/", NotesView.as_view(), name="notes"),
    path("creer/", CreateNoteView.as_view(), name="create"),
    path("modifier/<int:id>/", UpdateNoteView.as_view(), name="modifier")
]
