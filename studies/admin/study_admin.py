

from django.contrib import admin


class StudyAdmin(admin.ModelAdmin):

    def get_readonly_fields(self, request, obj):

        """
        Don't allow edits to the text after creation.
        """

        return self.readonly_fields + (
            ('text',) if obj else ()
        )
