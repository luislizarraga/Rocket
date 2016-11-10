from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from portal.views.security import LoginView, LogoutView

urlpatterns = [
    url(
        r'^login$',
        LoginView.as_view(),
        name='login'
    ),
    url(
        r'^logout$',
        LogoutView.as_view(),
        name='logout'
    )
]