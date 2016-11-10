from django.conf.urls import include, url

urlpatterns = [
    # url(r'^', include('portal.url_files.general')),
    # url(r'^', include('portal.url_files.conferences')),
    # url(r'^', include('portal.url_files.rooms')),
    # url(r'^', include('portal.url_files.invitations')),
    # url(r'^', include('portal.url_files.contacts')),
    # url(r'^', include('portal.url_files.cdr')),
    # url(r'^', include('portal.url_files.transactions')),
    url(r'^', include('portal.urls.security')),
    url(r'^', include('portal.urls.general')),
]
