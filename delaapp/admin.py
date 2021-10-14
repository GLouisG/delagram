from django.contrib import admin

from delaapp.models import Comment, Image, Profile


# Register your models here.
admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(Profile)