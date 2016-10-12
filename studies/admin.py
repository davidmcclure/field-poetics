

from django.contrib import admin

from studies.models import Text


class TextAdmin(admin.ModelAdmin):

    def get_readonly_fields(self, request, obj):

        """
        Don't allow edits to the markup after creation.
        """

        if obj:
            return self.readonly_fields + ('markup',)

        else:
            return self.readonly_fields


admin.site.register(Text, TextAdmin)
