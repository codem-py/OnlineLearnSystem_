from django.urls import path

from apps.views import HeatMapEntityApiView

urlpatterns = [
    path('student/activity', HeatMapEntityApiView.as_view()),
]
