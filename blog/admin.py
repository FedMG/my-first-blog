from django.contrib import admin
from .models import Post # De la misma carpeta(blog) (.) fichero(models) importamos(incluímos) el objeto 'Post' y lo hacemos visible en admin.py
# Register your models here.
admin.site.register(Post) # Lo registramos.
