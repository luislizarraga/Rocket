from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from portal.views.general import DashView, TicketCreate, TicketUpdate, RestrictedTicketUpdate

urlpatterns = [
    url(
        r'^$',
        login_required(DashView.as_view()),
        name='dashboard'
    ),
    url(
        r'^tickets/crear$',
        login_required(TicketCreate.as_view()),
        name='ticket_create'
    ),
    url(
        r'^tickets/editar/(?P<pk>\d+)$',
        login_required(TicketUpdate.as_view()),
        name='ticket_update'
    ),
    url(
        r'^tickets/usuario/editar/(?P<pk>\d+)$',
        login_required(RestrictedTicketUpdate.as_view()),
        name='ticket_update_restricted'
    ),
]