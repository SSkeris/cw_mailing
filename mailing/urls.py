from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from mailing.apps import MailingConfig
from mailing.views import MailingListView, MailingDetailView

appname = MailingConfig.name

urlpatterns = [
                  path('', MailingListView.as_view(), name='mailing_list'),
                  path('/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
