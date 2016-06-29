from django.test import TestCase
from email_responses.models import FromAddress


class ResponsesModelTestCase(TestCase):
    def test_model_from_address_to_str(self):
        instance = FromAddress(address='test@testaddress.com')
        self.assertEquals(str(instance), 'test@testaddress.com')
