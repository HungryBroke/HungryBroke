from django.contrib import admin

from account.models import Inventory, User

# Register your models here.

admin.site.register(User)
admin.site.register(Inventory)
