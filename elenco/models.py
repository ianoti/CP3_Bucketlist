from __future__ import unicode_literals

from django.db import models


class CommonFields(models.Model):
    """ The Bucketlist and Item classes will inherit from this class """
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ return a representation of the class """
        return self.title


class User(models.Model):
    """ the model definition for users of the application """
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return "User: {}{}".format(self.first_name, self.second_name)


class Bucketlist(CommonFields):
    """ the model definition for bucketlists belonging to a user """
    # user = models.ForeignKey(User, related_name="bucketlist")


class Item(CommonFields):
    """ the model definition for items in a bucketlist """
    status = models.BooleanField(default=False)
    bucket_list = models.ForeignKey(Bucketlist, related_name="item")
