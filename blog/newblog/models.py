from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=200, default="uncategorized")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home")
    
class Userprofile(models.Model):
    user = models.OneToOneField(User, null=True,on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic =models.ImageField(null=True,blank=True,upload_to="images/profile")

    def __str__(self):
        return str(self.user)

class Post(models.Model):
    title = models.CharField(max_length=200)
    header_image=models.ImageField(null=True,blank=True,upload_to="images/")

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #body = models.TextField()
    body = RichTextField(blank=True,null=True)
    post_date = models.DateField(auto_now_add=False)
    category = models.CharField(max_length=200, default="uncategorized")
    likes = models.ManyToManyField(User,related_name='blog_post')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("home")
    def total_likes(self):
        return self.likes.count()
