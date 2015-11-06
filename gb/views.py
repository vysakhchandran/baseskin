from __future__ import absolute_import
from django.views import generic
from django.contrib.auth.models import User
from .forms import RegistrationForm


class HomePageView(generic.TemplateView):
    template_name = 'home.html'

class SignUpView(generic.CreateView):
    form_class = RegistrationForm
    model = User
    template_name = 'accounts/signup.html'
