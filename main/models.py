from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile (models.Model):
    '''Extension of Django built-in User model'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    messages = models.ManyToManyField('main.Profile', through='Message')

    def __str__(self):
        return self.user.get_username()
    
    def get_absolute_url(self):
        return "/subject/%i/" % self.id


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    '''When user is created, attaches profile to it'''
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()


class Message(models.Model):
    text = models.TextField()
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='senders')
    recipient = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='recipients')

    def __str__(self):
        return self.text
    
    def get_absolute_url(self):
        return "/subject/%i/" % self.id
