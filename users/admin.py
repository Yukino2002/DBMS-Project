from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import *

# # Register your models here.
admin.site.register(CustomUser)
admin.site.register(Officer)
admin.site.register(Victim)