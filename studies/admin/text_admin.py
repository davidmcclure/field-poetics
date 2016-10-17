

from django.contrib import admin


class TextAdmin(admin.ModelAdmin):

    def get_readonly_fields(self, request, obj):

        """
        Don't allow edits to the markup after creation.
        """

        return self.readonly_fields + (
            ('markup',) if obj else ()
        )
