from django.urls import path
from .import views

urlpatterns = [
    path('', views.Blank, name='Blank'),
    path('index/', views.Index, name='Index'),
    path("getAdminLogin/", views.GetAdminLogin, name="GetAdminLogin"),
    path("adminHome/", views.AdminHome, name="AdminHome"),
    path("subjectSelect/", views.SubjectSelect, name="SubjectSelect"),
    path("studentList/", views.StudentList, name="StudentList"),
    path("getExamCreate/<subject>", views.GetExamCreate, name="etExamCreate"),
]
