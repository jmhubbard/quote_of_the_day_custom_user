from django.test import TestCase
from django.db import IntegrityError
from .models import Show, Episode
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

class EpisodeCreateTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Show.objects.create(name="a")
    def test_create_episode(self):
        show = Show.objects.get(name="a")
        Episode.objects.create(name="Episode Name", number=4, show=show)
    def test_episode_number_cannot_be_negative(self):
        show = Show.objects.get(name="a")
        with self.assertRaises(IntegrityError):
            Episode.objects.create(name="Episode Name", number=-4, show=show)