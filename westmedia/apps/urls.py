from django.urls import path
# from .views import MoviesView
from . import views

urlpatterns = [
    path("", views.MoviesView.as_view()),
]