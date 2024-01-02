

from django.test import TestCase,Client
from app.models import UserProfile, Quiz, question
from django.contrib.auth.models import User
from django.urls import reverse
import json
class UserProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_update_false_answers(self):
        user_profile = UserProfile.objects.create(user=self.user)
        user_profile.update_false_answers(5)
        self.assertEqual(user_profile.false_answers, 5)
    def test_update_correct_answers(self):
        user_profile = UserProfile.objects.create(user=self.user)
        user_profile.update_correct_answers(3)
        self.assertEqual(user_profile.correct_answers, 3)



