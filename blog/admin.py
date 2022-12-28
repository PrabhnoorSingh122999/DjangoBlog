from django.contrib import admin
from .models import Post
# Register your models here.

admin.site.register(Post)

admin.site.register(Health)
admin.site.register(Environment)
admin.site.register(Politics)
admin.site.register(Sports)
admin.site.register(Travel)
