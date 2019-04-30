from rest_framework import serializers
from . import models


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id', 
            'subject',
            'email_msg',
            'sender_email',
            'reciever_email',
            'sender_status',
            'reciever_status',
            'parent_msg_id',
        )
        model = models.Email