from django.shortcuts import render

from rest_framework import generics
from elenco.serializers import BucketlistSerializer
from elenco.models import Bucketlist


class CreateView(generics.ListCreateAPIView):
    """
    this class defines the create bucketlist behaviour of our Elenco API
    as well as the get all for the bucketlist.
    """
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        """ save the post data when creating a bucketlist"""
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    this class provides functionality to retrieve single bucketlist,
    update bucketlist, delete bucketlist
    """
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
