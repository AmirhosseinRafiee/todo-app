# from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class LoginView(LoginView):
    template_name = 'accounts/login.html'
    fields = ('username', 'password')
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("todo:task-list")