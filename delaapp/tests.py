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
    def test_save(self):
        self.profile.save_profile()
        the_profile = Profile.objects.all()
        self.assertTrue(len(the_profile)>0)
    def test_delete(self):
        self.profile.save_profile()      
        self.profile.delete_profile()
        self.assertTrue(len(Profile.objects.all())==0)