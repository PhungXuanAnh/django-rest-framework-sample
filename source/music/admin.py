import datetime
from django.contrib import admin
from music.models import Musician, Profile, Album, Instrument
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from admin_numeric_filter.admin import NumericFilterModelAdmin, SingleNumericFilter, RangeNumericFilter, SliderNumericFilter


class CustomSliderNumericFilter(SliderNumericFilter):
    MAX_DECIMALS = 2
    STEP = 10


class ProfileInline(admin.StackedInline):
    model = Profile
    extra = 0


@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', "email", "instruments"]
    list_display = ('first_name', 'last_name', "email", "created_at")
    list_filter = ( 
        "created_at",
        ("created_at", DateTimeRangeFilter),
        "first_name", 
        "last_name",
        )
    search_fields = ("first_name", "last_name", "email")
    inlines = [ProfileInline]
    # NOTE: refe ModelAdmin for more already define attributes

    # If you would like to add a default range filter
    # method pattern "get_rangefilter_{field_name}_default"
    def get_rangefilter_created_at_default(self, request):
        return (datetime.datetime.now(), datetime.datetime.now())

    # If you would like to change a title range filter
    # method pattern "get_rangefilter_{field_name}_title"
    def get_rangefilter_created_at_title(self, request, field_path):
        return 'By created_at date time range'

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date', "num_stars")
    list_filter = (
        "release_date",
        ("release_date", DateRangeFilter),
        ('num_stars', SingleNumericFilter), # Single field search, __gte lookup
        ('num_stars', RangeNumericFilter), # Range search, __gte and __lte lookup
        # ('num_stars', SliderNumericFilter), # Same as range above but with slider
        # ('num_stars', CustomSliderNumericFilter), # Filter with custom attributes
        # "num_stars",
        "name"
    )
    search_fields = ('name', 'release_date', "num_stars")
    # NOTE: refe ModelAdmin for more already define attributes

    # If you would like to add a default range filter
    # method pattern "get_rangefilter_{field_name}_default"
    def get_rangefilter_release_date_default(self, request):
        return (datetime.date.today, datetime.date.today)

    # If you would like to change a title range filter
    # method pattern "get_rangefilter_{field_name}_title"
    def get_rangefilter_release_date_title(self, request, field_path):
        return 'By release date range'

@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    list_display = ('name',)

# admin.site.register(Musician, MusicianAdmin)
# admin.site.register(Album, AlbumAdmin)
# admin.site.register(Instrument, InstrumentAdmin)
