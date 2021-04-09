from django.contrib import admin
from music.models import Musician, Profile, Album, Instrument

class ProfileInline(admin.StackedInline):
    model = Profile
    extra = 0


@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', "email", "instruments"]
    list_display = ('first_name', 'last_name', "email", "created_at")
    list_filter = ("first_name", "last_name", "created_at")
    search_fields = ("first_name", "last_name", "email")
    inlines = [ProfileInline]
    # NOTE: refe ModelAdmin for more already define attributes

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date', "num_stars")
    list_filter = (
        "release_date",
        "num_stars",
        "name"
    )
    search_fields = ('name', 'release_date', "num_stars")
    # NOTE: refe ModelAdmin for more already define attributes

    def get_rangefilter_release_date_title(self, request, field_path):
        return 'release date range'

@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    list_display = ('name',)

# admin.site.register(Musician, MusicianAdmin)
# admin.site.register(Album, AlbumAdmin)
# admin.site.register(Instrument, InstrumentAdmin)
