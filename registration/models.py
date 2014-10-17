from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(AbstractUser):
    MALE = 'M'
    FEMALE = 'F'
    MALE_FEMALE_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    male_female = models.CharField(max_length=1, choices=MALE_FEMALE_CHOICES)
    looking_for_male_female = models.CharField(max_length=1, choices=MALE_FEMALE_CHOICES)
    paid_user = models.BooleanField(default=False)

    def __unicode__(self):
        return self.username


class ProfilePicture(models.Model):
    image = models.ImageField(upload_to='media/profile_picutures',
                              blank=True,
                              null=True)
    description = models.CharField(max_length=140,
                                   blank=True,
                                   null=True)
    profile = models.ForeignKey(Profile, related_name='profile_pictures')