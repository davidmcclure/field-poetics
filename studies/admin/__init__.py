

from django.contrib import admin

from studies.models import Text
from studies.models import Study

from .text_admin import TextAdmin


admin.site.register(Text, TextAdmin)
admin.site.register(Study)
