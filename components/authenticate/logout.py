from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout


def signout(request):
    logout(request) 
    messages.success(request, "Logged Out Successfully!")
    return redirect('index') 
  