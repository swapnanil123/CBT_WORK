from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

from django.contrib import messages
# Create your views here.


def Login(request):

    if request.method == 'POST':
        context = dict()

        username = request.POST['username']
        password = request.POST['pass']

        context['userName'] = username

        # print(context)

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/adminHome', context)

        else:
            messages.success(request,"Username and Password not matched")
            return redirect ('/getAdminLogin')           
            
    
    return redirect('/getAdminLogin')



def Logout(request):
    auth.logout(request)
    return redirect('/getAdminLogin')