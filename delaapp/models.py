from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    dp = models.ImageField(upload_to = 'profiles/', default='SOME STRING')
    bio = models.TextField(max_length=500, default=f'This is my bio, Welcome!')
    following = models.ManyToManyField(User, blank=True, related_name='followers')
    
    def __str__(self):
          return f'{self.user.username}'

    def save_profile(self):
           self.save()
    def delete_profile(self):
           self.delete()     
    def bio_updater(self, new_bio):
           self.bio = new_bio
           self.save()      

# class Image(models.Model):
#   image = models.ImageField(upload_to='images/')
#   caption = models.TextField()
#   owner = models.ForeignKey('Profile', on_delete=models.CASCADE)
#   likes = models.ManyToManyField(User, blank=True)
#   pub_date = models.DateTimeField(auto_now_add=True)

#   def __str__(self):
#     return self.caption
    

#   def updater(self, cap):
#     try:
#       self.caption = cap
#       self.save()
#       return self
#     except self.DoesNotExist:
#       print('The caption does not exist in our records')

# class Comment(models.Model):
#   postde = models.ForeignKey('Image', on_delete=models.CASCADE)
#   owner = models.ForeignKey('Profile', on_delete=models.CASCADE)
#   content = models.TextField()
#   pub_date = models.DateTimeField(auto_now_add=True)

#   def __str__(self):
#     return self.content  

# class Foll(models.Model):
#     target = models.ForeignKey('User', related_name='followers')
#     follower = models.ForeignKey('User', related_name='targets')
#     def __str__(self):
#      return self.target