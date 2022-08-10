from django.urls import path, include
from . import views

app_name = "AttendanceLeaveApp"

urlpatterns = [
    path('', views.attendanceView.as_view(), name="attendance")
]
