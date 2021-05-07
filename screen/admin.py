from django.contrib import admin
from screen.models import UnlockScreenUrl


@admin.register(UnlockScreenUrl)
class MusicianAdmin(admin.ModelAdmin):
    pass
