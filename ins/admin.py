from django.contrib import admin
from ins.models import Post, InstaUser, Like


# Register your models here.
admin.site.register(InstaUser)
admin.site.register(Post)
admin.site.register(Like)
