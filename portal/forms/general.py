# -*- coding: utf-8 -*-
from django.forms import ModelForm, CharField, PasswordInput, Select, Textarea
from tickets.models import Ticket

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['status', 'assigned_user', 'description', 'notes']
        widgets = {
            'status': Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'assigned_user': Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'description': Textarea(
                attrs={
                    'class': 'form-control',
                }
            ),
            'notes': Textarea(
                attrs={
                    'class': 'form-control',
                }
            )
        }
        labels = {
            'status': u'Status',
            'assigned_user': u'Usuario asignado',
            'description': u'Descripción',
            'notes': u'Notas'
        }


class RestrictedTicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['status', 'description', 'notes']
        widgets = {
            'status': Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'description': Textarea(
                attrs={
                    'class': 'form-control',
                    'readonly': True
                }
            ),
            'notes': Textarea(
                attrs={
                    'class': 'form-control',
                }
            )
        }
        labels = {
            'status': u'Status',
            'description': u'Descripción',
            'notes': u'Notas',
        }