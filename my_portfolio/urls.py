from django.urls import path
from . import views

urlpatterns = [
    path("", views.DetailProfileView.as_view(),  name="resume"),
    path("blog/<str:slug>/", views.DetailArticlesView.as_view(), name="blog"),
]