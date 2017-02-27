from django.test import TestCase
from elenco.models import Bucketlist


class ModelTestCase(TestCase):
    """ Tests for the models of the bucketlist application elenco"""

    def setUp(self):
        """ the initialisation of the tests"""
        self.bucketlist = Bucketlist(title="just a test")

    def test_bucketlist_model(self):
        """ test that model can create a bucketlist"""
        old_count = Bucketlist.objects.count()
        self.bucketlist.save()
        new_count = Bucketlist.objects.count()
        self.assertEqual(new_count-old_count, 1)
