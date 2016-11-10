# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.forms import Form, CharField, PasswordInput
from django.views.generic import FormView, View
from django.contrib.auth.models import User
from portal.forms.security import LoginForm
from django.shortcuts import redirect
from django.contrib import messages


class LoginView(FormView):
    template_name = 'portal/security/login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if user is not None:
            login(self.request, user)
        else:
            messages.add_message(self.request, messages.ERROR, u'Los datos de inicio de sesión son incorrectos')
        return super(LoginView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')