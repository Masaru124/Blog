from django.contrib import admin
from .models import Post,Category,Userprofile
 
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Userprofile)