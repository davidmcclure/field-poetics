

from django.contrib import admin

from studies.models import Study

from .study_admin import StudyAdmin


admin.site.register(Study, StudyAdmin)
