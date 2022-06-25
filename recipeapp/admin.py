from django.contrib import admin
from .models import Post, sweetdb, vegetabledb, maincoursedb

# Register your models here.

admin.site.register(Post)
admin.site.register(sweetdb)
admin.site.register(vegetabledb)
admin.site.register(maincoursedb)