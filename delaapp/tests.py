from datetime import datetime
from django.contrib.auth.models import User
from django.test import TestCase

from delaapp.models import Comment, Image, Profile

# Create your tests here.
class UserProfileTestClass(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="Johnny")
        self.profile = Profile(user=self.user, picture="test.jpg", bio = "A description" )    

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
