from django.contrib import admin
from .models import Profile


class ProfilesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile, ProfilesAdmin)

# Register your models here.
