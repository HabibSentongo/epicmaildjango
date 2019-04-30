from django.db import models
from django.contrib.auth.models import User


SENDER_CHOICES = (
    ('s', 'Sent'),
    ('d', 'Draft'),
)

RECIEVER_CHOICES = (
    ('u', 'Unread'),
    ('r', 'Read'),
)


class Email(models.Model):
    """
    Email Model
    Defines the attributes of an Email message
    """
    subject = models.CharField(max_length=100)
    email_msg = models.TextField()
    registered = models.DateTimeField(auto_now_add=True, editable=False)
    sender_email = models.EmailField(unique=True)
    reciever_email = models.EmailField(unique=True)
    sender_status = models.CharField(choices=SENDER_CHOICES, max_length=1, default='s')
    reciever_status = models.CharField(choices=RECIEVER_CHOICES, max_length=1, default='u')
    parent_msg_id = models.IntegerField(default=0)

# class UserProfile(models.Model):
#     user = models.OneToOneField(User)

#     phone_number = models.IntegerField(max_length=15)
#     # user image/ profile photo
#     # profile_pic = models.ImageField(upload_to='profile_images', blank=True)

#     def __unicode__(self):
#         return self.user.username