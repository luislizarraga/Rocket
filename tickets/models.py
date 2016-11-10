# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    method_choices = (
        ('Abierto', 'Abierto'),
        ('Pendiente', 'Pendiente'),
        ('Cerrado', 'Cerrado'),
    )

    assigned_user = models.ForeignKey(User, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        blank=False,
        null=False,
        choices=method_choices,
        max_length=100,
        default='Abierto'
    )
    description = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

