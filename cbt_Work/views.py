
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
# Create your views here.


def Blank(request):
    return redirect('index/')


def Index(request):
    return render(request, 'cbt_work/index.html')


def GetAdminLogin(request):
    return render(request, 'cbt_work/adminView/adminLoginPage.html')


def AdminHome(request):
    return render(request, 'cbt_work/adminView/adminHome.html')


def SubjectSelect(request):
    return render(request, 'cbt_work/adminView/subjectSelect.html')


def StudentList(request):
    return render(request, 'cbt_work/adminView/studentList.html')


def GetExamCreate(request, subject=''):
    return render(request, 'cbt_work/adminView/examCreate.html')