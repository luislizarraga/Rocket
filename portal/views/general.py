# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404, StreamingHttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, ListView, CreateView, UpdateView
from portal.forms.general import TicketForm, RestrictedTicketForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.urlresolvers import reverse, reverse_lazy
from datetime import datetime, time, date, timedelta
from django.contrib import messages
from django.core import exceptions
from tickets.models import *


class DashView(View):
    def get(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_superuser:
            tickets = Ticket.objects.exclude(status = 'Cerrado')

        else:
            tickets = Ticket.objects.filter(assigned_user = user)\
                        .exclude(status = 'Cerrado')


        return render(request, 'portal/general/dash.html', {
            'user': user,
            'tickets': tickets,
            # 'client_last_month_data': client_last_month_data,
            # 'year': start.year,
            # 'month': start.month,
            # 'first': first,
            # 'asr': asr,
            # 'acd': acd,
            # 'payments' : payments,
            # 'currency': client.get_currency()
        })


class TicketCreate(PermissionRequiredMixin, CreateView):
    context_object_name = 'ticket'
    model = Ticket
    template_name = 'portal/tickets/create.html'
    form_class = TicketForm
    permission_required = 'tickets.add_ticket'

    def form_valid(self, form):
        messages.success(self.request, u'¡Enhorabuena! Ticket creado exitosamente.')
        return super(TicketCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('portal:dashboard')


class TicketUpdate(PermissionRequiredMixin, UpdateView):
    context_object_name = 'ticket'
    model = Ticket
    template_name = 'portal/tickets/update.html'
    form_class = TicketForm
    permission_required = 'tickets.add_ticket'

    def form_valid(self, form):
        messages.success(self.request, u'¡Enhorabuena! Ticket editado exitosamente.')
        return super(TicketUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('portal:dashboard')


class RestrictedTicketUpdate(UpdateView):
    context_object_name = 'ticket'
    model = Ticket
    template_name = 'portal/tickets/update_restricted.html'
    form_class = RestrictedTicketForm

    def form_valid(self, form):
        messages.success(self.request, u'¡Enhorabuena! Ticket editado exitosamente.')
        return super(RestrictedTicketUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('portal:dashboard')