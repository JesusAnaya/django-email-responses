from django.template import Context, Template
from .models import Response
from .utils import get_destinations, send_html_email
import logging

logger = logging.getLogger(__name__)


def send_email(token, context={}, to=None):
    try:
        response = Response.objects.get(token=token)
        message = Template(response.content).render(Context(context))

        # Get destination address list
        if to:
            to_address = [to]
        else:
            to_address = get_destinations(response.id, 'to')

        cc = get_destinations(response.id, 'cc')
        bcc = get_destinations(response.id, 'bcc')

        subject = response.subject
        from_email = response.from_address.address

        send_html_email(subject, from_email, message, to_address, cc, bcc)

    except Response.DoesNotExist:
        print("Does not exist a response with token %s" % token)
