from django.contrib import admin
from .models import Translation

@admin.register(Translation)
class TranslationAdmin(admin.ModelAdmin):
    list_display = ('text', 'translated_text', 'source_language', 'dest_language', 'created_at')
    search_fields = ('text', 'translated_text', 'source_language', 'dest_language')
    list_filter = ('source_language', 'dest_language', 'created_at')
