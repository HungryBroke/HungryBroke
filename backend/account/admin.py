from django.contrib import admin

from account.models import Inventory, Profile

# Register your models here.

admin.site.register(Profile)
admin.site.register(Inventory)
