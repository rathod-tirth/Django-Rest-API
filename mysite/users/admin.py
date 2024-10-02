from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.
admin.site.register(MyUser, UserAdmin)


@admin.register(BackendUser)
class BackendUserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "email"]
    list_filter = ["is_admin", "email"]
    fieldsets = (
        (None, {"fields": ["email"]}),
        (
            "Personal Info",
            {
                "classes": "wide",
                "fields": [
                    ("first_name", "last_name"),
                    ("date_of_birth", "gender"),
                    "address",
                ],
            },
        ),
        (
            "Permissions",
            {
                "classes": "wide",
                "fields": ["is_admin"],
            },
        ),
    )
