from rest_framework import serializers
from . import models

class FriendSerializers(serializers.ModelSerializer):
    """Serialize the Friend Model

    Arguments:
        serializers {ModelSerializer} -- Gives access to the id, and name fields
    """ 

    class Meta:
        model = models.Friend
        fields = ('id', 'name')


class BelongingSerializer(serializers.ModelSerializer):
    """Serialize the Belonging Model

    Arguments:
        serializers {ModelSerializer} -- Gives access to the id, and name fields
    """ 

    class Meta:
        model = models.Belonging
        fields = ('id', 'name')


class BorrowedSerializer(serializers.ModelSerializer):
    """Serialize the Borrowed Model

    Arguments:
        serializers {ModelSerializer} -- Gives access to the id, 
        'what', 'to_who', 'when', 'returned'
    """ 

    class Meta:
        model = models.Borrowed
        fields = ('id', 'what', 'to_who', 'when', 'returned')

