

from django.contrib import admin

from studies.models import Text

from .text_admin import TextAdmin


admin.site.register(Text, TextAdmin)
