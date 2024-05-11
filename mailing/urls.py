from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView, MailingDeleteView, \
    ClientListView, ClientCreateView, ClientUpdateView, MessageListView, MessageCreateView, MessageUpdateView

appname = MailingConfig.name

urlpatterns = [
                  path('', MailingListView.as_view(), name='mailing_list'),

                  path('/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
                  path('create_mailing/', MailingCreateView.as_view(), name='mailing_form'),
                  path('<int:pk>/update', MailingUpdateView.as_view(), name='mailing_update'),
                  path('<int:pk>/delete', MailingDeleteView.as_view(), name='mailing_delete'),

                  path('clients/', ClientListView.as_view(), name='clients_list'),
                  path('create_client/', ClientCreateView.as_view(), name='clients_form'),
                  path('<int:pk>/update_client/', ClientUpdateView.as_view(), name='client_update'),

                  path('messages/', MessageListView.as_view(), name='message_list'),
                  path('create_message/', MessageCreateView.as_view(), name='message_form'),
                  path('<int:pk>/update_message/', MessageUpdateView.as_view(), name='message_update'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
