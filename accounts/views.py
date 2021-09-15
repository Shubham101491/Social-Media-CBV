from django.shortcuts import render
from django.views.generic import TemplateView,CreateView

from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse_lazy

# 
from django.http import HttpResponseRedirect
from django.urls import reverse

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class TestPage(TemplateView):
    template_name = 'accounts/test.html'
    

class ThanksPage(TemplateView):
    template_name = 'accounts/thanks.html'

class Home(TemplateView):
    template_name = 'accounts/index.html'

    # def get(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         return HttpResponseRedirect(reverse("test"))
    #     return super().get(request, *args, **kwargs)