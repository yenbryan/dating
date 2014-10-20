from django.db import models
from django.contrib.auth.models import AbstractUser


class Dater(AbstractUser):
    gender_male = models.BooleanField(default=True)
    gender_preference_male = models.BooleanField(default=True)
    occupation = models.CharField(max_length=50, blank=True)
    age = models.IntegerField(max_length=2, null=True, blank=True)
    height = models.CharField(max_length=20, null=True, blank=True)
    weight = models.IntegerField(max_length=4, null=True, blank=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    profile_image = models.ImageField(upload_to='profile_pictures', null=True, blank=True)

    def __unicode__(self):
        return u"{}".format(self.username)


class Image(models.Model):
    title = models.CharField(max_length=50, blank=True)
    picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    dater_image = models.ForeignKey(Dater, related_name="images")

    def __unicode__(self):
        return u"{}".format(self.title)


class Match(models.Model):
    #user selection options:
        #1 = bump_into
        #2 = bumped to curb
        #3 = bumpin

    user1 = models.ForeignKey(Dater, related_name='matches')
    user2 = models.ForeignKey(Dater, related_name='user_2_match')
    user1_select = models.IntegerField()
    user2_select = models.IntegerField()

    def __unicode__(self):
        return u"{} rated {}".format(self.user1, self.user2)


class Chat(models.Model):
    message = models.TextField()
    sender = models.ForeignKey(Dater, related_name='user_sender')
    recipient = models.ForeignKey(Dater, related_name='user_recipient')
    time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"{} messaged {}".format(self.sender, self.recipient)