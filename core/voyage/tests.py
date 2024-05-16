from django.test import TestCase
from .models import Voyage

class VoyageTestCase(TestCase):
    fixtures = Voyage
