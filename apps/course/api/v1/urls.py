from django.urls import path, include
from .views import CourseListView, CourseCreateView, CourseRudView, LessonListView, LessonCreateView, LessonRudView

urlpatterns = [
    path('list/', CourseListView.as_view()),
    path('create/', CourseCreateView.as_view()),
    path('rud/<int:pk>/', CourseRudView.as_view()),
    path('course/<int:course_id>/lessons/list/', LessonListView.as_view()),
    path('course/<int:course_id>/lessons/create/', LessonCreateView.as_view()),
    path('course/<int:course_id>/lessons/rud/<int:pk>/', LessonRudView.as_view()),
]