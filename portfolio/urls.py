from django.urls import path

from . import views

urlpatterns = [
    path("", views.perfil, name="perfil"),
    path("contato/", views.contato, name="contato"),
    path("curriculo/", views.curriculo, name="curriculo"),
    path("baixar/<slug:slug>/", views.baixar, name="baixar"),
]
