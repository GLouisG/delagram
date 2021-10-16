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

class ImageTestClass(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="Johnny")
        self.user.save()
        self.profile = Profile(user=self.user, picture="test.jpg", bio = "A description" )
        self.profile.save_profile()
        self.test_img = Image(image="test.jpg", caption="caption", owner=self.profile, pub_date=datetime.now())  
        self.test_img.save_image()  

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
        Image.objects.all().delete()
    def test_delete(self):     
        self.test_img.delete_image()
        self.assertTrue(len(Image.objects.all())==0) 
    def test_updater(self):
        updated = self.test_img.updater('Hi')
        self.assertEqual(updated.caption, 'Hi')                       
    def test_search(self):
        img = Image.img_searcher('caption')
        self.assertTrue(len(img)>0)         

class CommentTestClass(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="Johnny")
        self.user.save()
        self.profile = Profile(user=self.user, picture="test.jpg", bio = "A description" )
        self.profile.save_profile()
        self.test_img = Image(image="test.jpg", caption="caption", owner=self.profile, pub_date=datetime.now())  
        self.test_img.save_image()  
        self.test_comm = Comment(postde=self.test_img, owner=self.profile,content="content", pub_date=datetime.now())
        self.test_comm.save_comment()

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
        Image.objects.all().delete()
        Comment.objects.all().delete()
    def test_delete(self):     
        self.test_comm.delete_comment()
        self.assertTrue(len(Comment.objects.all())==0)        