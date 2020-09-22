from django.test import TestCase
from django.db import IntegrityError
from .models import Show
# Create your tests here.
class ShowNameTestCase(TestCase):
    def test_show_name_is_unique(self):
        with self.assertRaises(IntegrityError):
            Show.objects.create(name="a")
            Show.objects.create(name="a")


class ShowNameUniquenessTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Show.objects.create(name="a")

    def test_show_name_is_unique(self):
        with self.assertRaises(IntegrityError):
            Show.objects.create(name="a")
