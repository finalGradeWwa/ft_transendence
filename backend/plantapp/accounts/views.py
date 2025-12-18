from django.shortcuts import redirect, render
from django import forms

# Create your views here.

# accounts/views.py

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "sign_up.html"


def login_view(request):
    form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})
