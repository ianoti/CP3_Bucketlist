from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse


class ApiViewTestCase(TestCase):
    """ the API views are tested here"""

    def setUp(self):
        """ the test setup"""
        self.client = APIClient()
        self.bucketlist_data = {"title": "just a test"}

    def test_can_create_bucketlist(self):
        response = self.client.post(reverse("create"), self.bucketlist_data,
                                    format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
