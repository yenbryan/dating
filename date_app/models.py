from django.db import models
from registration.models import Profile
# from django.contrib.auth.models import AbstractUser
#
#
# # Create your models here.
# class Dater(AbstractUser):
#     gender_male = models.BooleanField(default=True)
#     gender_preference_male = models.BooleanField(default=True)
#     occupation = models.CharField(max_length=50, blank=True)
#     age = models.IntegerField(max_length=2, null=True, blank=True)
#     height = models.CharField(max_length=20)
#     weight = models.IntegerField(max_length=4, null=True, blank=True)
#     latitude = models.CharField(max_length=50)
#     longitude = models.CharField(max_length=50)
#     profile_image = models.ImageField(upload_to='traveler_images', null=True, blank=True)
#
#     def __unicode__(self):
#         return u"{}".format(self.username)
#
#
# class Image(models.Model):
#     title = models.CharField(max_length=50, blank=True)
#     picture = models.ImageField(upload_to='traveler_images', null=True, blank=True)
#     dater_image = models.ForeignKey(Dater, related_name="an_image")
#
#     def __unicode__(self):
#         return u"{}".format(self.title)



class Match(models.Model):
    user1 = models.ForeignKey(Profile, related_name='match_user1')
    user2 = models.ForeignKey(Profile, related_name='matchmade')
    user1_select = models.IntegerField()
    user2_select = models.IntegerField()

    def __unicode__(self):
        return u"{} rated {}".format(self.user1, self.user2)
