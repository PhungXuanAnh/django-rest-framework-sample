from django.contrib import admin
from music.models import Musician, Profile, Album, Instrument


class ProfileInline(admin.StackedInline):
    model = Profile
    extra = 0


class MusicianAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', "email", "instruments"]
    list_display = ('first_name', 'last_name', "email")
    inlines = [ProfileInline]


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date', "num_stars")

class InstrumentAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Musician, MusicianAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Instrument, InstrumentAdmin)
