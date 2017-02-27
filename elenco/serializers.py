from rest_framework import serializers
from elenco.models import Bucketlist


class BucketlistSerializer(serializers.ModelSerializer):
    """ convert the Bucketlist model to a JSON format for API"""
    class Meta:
        """
        modifies class behaviour to make the output appear in JSON format
        """
        model = Bucketlist
        fields = ('id', 'title', 'description', 'date_created',
                  'date_modified')
        # specify fields user cannot edit as system will set them
        read_only_fields = ('date_created', 'date_modified')
