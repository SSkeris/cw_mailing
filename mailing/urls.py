from django.contrib import admin
from django.urls import path, include

from mailing.apps import MailingConfig

appname = MailingConfig.name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mailing.urls', namespace='mailing')),
]