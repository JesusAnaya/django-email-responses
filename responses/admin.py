from django.contrib import admin
from .models import Response, Destination, FromAddress

# Compatible with Mezzanine CMS Framework
#
try:
    from mezzanine.core.admin import TabularDynamicInlineAdmin
    TABULAR_CLASS = TabularDynamicInlineAdmin
except ImportError:
    from django.contrib.admin import TabularInline
    TABULAR_CLASS = TabularInline


class DestinationInline(TABULAR_CLASS):
    model = Destination
    extra = 1


class ResponseAdmin(admin.ModelAdmin):
    list_display = ('token', 'subject', 'from_address')
    inlines = (DestinationInline,)


admin.site.register(FromAddress)
admin.site.register(Response, ResponseAdmin)
