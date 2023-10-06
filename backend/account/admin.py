from django.contrib import admin

from account.models import Inventory, Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user",)  # display user in list

    # make models name more readable in admin interface
    def __str__(self):
        return self.user.username


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "user",
    )  # display name and user in list

    # make models name more readable in admin interface
    def __str__(self):
        return self.name


# Register your models here.
