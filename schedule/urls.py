from django.urls import path
from . import views

urlpatterns = [
    path("", views.ScheduleView.as_view()),
    path("<int:pk>/", views.ScheduleDetailView.as_view()),
]
