from django.contrib import admin
from home.models import User,Books

# Register your models here.
admin.site.register((User,Books))