from django.contrib import admin
from .models import Response, Destination, FromAddress
from .forms import ResponseForm

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
    class Media:
        js = (
            '/static/responses/tiny_mce/tinymce.min.js',
            '/static/responses/tinymce.js',
        )

    form = ResponseForm
    list_display = ('token', 'subject', 'from_address', 'alternative_from')
    inlines = (DestinationInline,)


admin.site.register(Response, ResponseAdmin)
admin.site.register(FromAddress)
