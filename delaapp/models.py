from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    picture = models.ImageField(upload_to = 'profiles/', default='profile.jpg')
    bio = models.TextField(max_length=500, default=f'This is my bio, Welcome!')
    following = models.ManyToManyField(
      #User, blank=True, related_name='followers'
      "self", blank=True, related_name="followers", symmetrical=False
      )
    
    def __str__(self):
          return f'Profile {self.user.username}'

    def save_profile(self):
           '''Saves profiles'''
           self.save()
    def delete_profile(self):
           '''Deletes profiles''' 
           self.delete()     
    def bio_updater(self, new_bio):
           '''Updates bios'''
           self.bio = new_bio
           self.save()  
    def pic_update(self, photo):
           ''' method to update a profile picture '''
           self.picture = photo
           self.save()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Image(models.Model):
  # image = models.ImageField(upload_to = 'images/',)
  image = CloudinaryField('image')
  caption = models.TextField()
  owner = models.ForeignKey('Profile', on_delete=models.CASCADE)
  likes = models.ManyToManyField(User, blank=True)
  pub_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'Image {self.caption}'

  def save_image(self):
      '''Saves the image'''
      self.save()
  def delete_image(self):
      '''Deletes the image'''
      self.delete()      

  def updater(self, cap):
      ''' Updates the image caption'''
      try:
        self.caption = cap
        self.save()
        return self
      except self.DoesNotExist:
        print('The caption does not exist in our records')
  @classmethod
  def img_searcher(cls, search_term):
    search_term= str(search_term)
    photos = cls.objects.filter(caption__contains = search_term)
    return photos          


class Comment(models.Model):
  postde = models.ForeignKey('Image',related_name="comments", on_delete=models.CASCADE)
  owner = models.ForeignKey('Profile', on_delete=models.CASCADE)
  content = models.TextField()
  pub_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return "Comment{self.content}"  
  def save_comment(self):
      '''Saves the comment'''
      self.save()
  def delete_comment(self):
      '''Deletes the comment'''
      self.delete()      
  def change_comment(self, new_comment):
      ''' method to change a comment'''
      self.content = new_comment
      self.save()        

# class Foll(models.Model):
#     target = models.ForeignKey('User', related_name='followers')
#     follower = models.ForeignKey('User', related_name='targets')
#     def __str__(self):
#      return self.target