from django.urls import path
from .views import *
from api import views

urlpatterns = [
    path('', getRoutes, name="routes"),
    path('notes/', getNotes, name="notes"),
    path('notes/<str:pk>/update/', updateNote, name="update-note"),
    path('notes/<str:pk>/delete/', deleteNote, name="delete-note"),
    path('notes/create/', createNote, name="create-note"),
    path('notes/<str:pk>/', getNote, name="note"),
    # urls.py
    path('github-webhook/', views.github_webhook)

]