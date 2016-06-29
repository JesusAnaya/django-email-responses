from django.core.mail import EmailMultiAlternatives
from django.template import Context, Template
from django.utils.html import strip_tags
from .models import Destination
import logging

logger = logging.getLogger(__name__)


def get_destinations(response_id, send_type, context={}):
    d = Destination.objects.filter(response=response_id, send_type=send_type)
    return [Template(x.address).render(Context(context)) for x in d]


def send_html_email(subject, from_email, content, to, cc=None, bcc=None):
    text_content = strip_tags(content)
    html_content = content
    msg = EmailMultiAlternatives(subject, text_content, from_email,
                                                to, cc=cc, bcc=bcc)

    msg.attach_alternative(html_content, "text/html")
    msg.send()
