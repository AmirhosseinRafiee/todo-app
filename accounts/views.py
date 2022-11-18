from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class LoginView(LoginView):
    template_name = 'accounts/login.html'
    fields = ('username', 'password')
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("todo:task-list")

class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy("accounts:login")

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().get(request, *args, **kwargs)