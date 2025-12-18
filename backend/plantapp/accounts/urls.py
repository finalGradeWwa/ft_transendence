from django.urls import path
from .views import SignUpView, login_view

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
	path("login/", login_view, name="login"),
]