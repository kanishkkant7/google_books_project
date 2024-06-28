from django.shortcuts import render
from .forms import AuthForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

class loginView(LoginView):
    form_class=AuthForm
    template_name="registration/login.html"
class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)