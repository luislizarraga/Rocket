# -*- coding: utf-8 -*-
from django.forms import Form, CharField, PasswordInput

class LoginForm(Form):
    username = CharField()
    password = CharField(widget=PasswordInput, max_length=200)