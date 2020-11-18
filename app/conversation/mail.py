from django.db import connection
from django_globals import globals
from django.conf import settings
from django.template import Context
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django_tenants.utils import get_tenant_model, tenant_context

class Notifications():
    def __init__(self):
        pass

    def notification(self, chat):
        sender_id = chat.user.id
        recevier_id = chat.client.id if chat.operator.id == sender_id else chat.operator.id
        sender_user = User.objects.get(id = sender_id)
        receiver_user = User.objects.get(id = receiver_id)

        sub ="Promo code for the product"
        body = chat.message
        
        email = EmailMessage(
            sub,
            body,
            [sender_user.email],
            [receiver_user.email],
            headers={'Message-ID': 'Cartloop'}
        )        

        email.send()