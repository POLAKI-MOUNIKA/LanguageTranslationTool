from django.db import models
from django.db import models

class Translation(models.Model):
    text = models.TextField()
    translated_text = models.TextField()
    source_language = models.CharField(max_length=10)
    dest_language = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f'{self.text[:50]}... -> {self.translated_text[:50]}...'
