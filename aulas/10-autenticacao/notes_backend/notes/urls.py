from django.urls import path

from . import views

urlpatterns = [
    path('api/notes/<int:note_id>/', views.api_note),
    path('api/notes/', views.api_note_list),
]
