from django.db import models

DESTINATION_TYPES = (
    ('to', 'To'),
    ('cc', 'Cc'),
    ('bcc', 'Bcc'),
)


class FromAddress(models.Model):
    address = models.EmailField()

    def __unicode__(self):
        return self.address


class Response(models.Model):
    token = models.CharField(max_length=255)
    from_address = models.ForeignKey(FromAddress, verbose_name="From")
    subject = models.CharField(max_length=255)
    content = models.TextField()

    def __unicode__(self):
        return self.token


class Destination(models.Model):
    response = models.ForeignKey(Response)
    send_type = models.CharField(max_length=5, choices=DESTINATION_TYPES)
    address = models.EmailField()
