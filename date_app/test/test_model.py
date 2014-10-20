from django.test import TestCase
from date_app.models import Dater, Image, Match


class ModelTestCase(TestCase):
    def setUp(self):
        self.user1 = Dater.objects.create(
            username='user1',
            email='u1@test.com',
            first_name='u',
            last_name='1',
            password='1',
            gender_male = True,
            gender_preference_male = False,
            occupation = "",
            age = 21,
            height = '50',
            weight = 150,
            latitude = 12.234,
            longitude = 12.234,
            profile_image = '',
        )
        self.user2 = Dater.objects.create(
            username='user2',
            email='u2@test.com',
            first_name='u',
            last_name='2',
            password='1',
            gender_male = False,
            gender_preference_male = True,
            occupation = "",
            age = 21,
            height = '50',
            weight = 150,
            latitude = 12.234,
            longitude = 12.234,
            profile_image = '',
        )
        self.match = Match.objects.create(
            user1=self.user1,
            user2=self.user2,
            user1_select=1,
            user2_select=1,
        )

    def test_dater_profile_model_uicode(self):
        self.assertEqual(self.user1.__unicode__(), 'user1')

    def test_match_model_unicode(self):
        self.assertEqual(self.match.__unicode__(), 'user1 rated user2')
