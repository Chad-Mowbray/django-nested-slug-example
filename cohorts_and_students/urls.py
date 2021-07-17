from django.urls import path
from . import views

urlpatterns = [
    path('', views.cohort_list, name='cohort_list'),
    path('new', views.new_cohort, name='new_cohort'),
    path('<uuid:cohort_uuid>', views.cohort_detail, name='cohort_detail'),
    path('<uuid:cohort_uuid>/edit', views.edit_cohort, name='edit_cohort'),
    path('<uuid:cohort_uuid>/delete', views.delete_cohort, name='delete_cohort'),
    path('<uuid:cohort_uuid>/students', views.student_list, name='student_list'),
    path('<uuid:cohort_uuid>/students/new', views.new_student, name='new_student'),
    path('<uuid:cohort_uuid>/students/<slug:student_slug>', views.student_detail, name='student_detail'),
    path('<uuid:cohort_uuid>/students/<slug:student_slug>/edit', views.edit_student, name='edit_student'),
    path('<uuid:cohort_uuid>/students/<slug:student_slug>/delete', views.delete_student, name='delete_student'),
]