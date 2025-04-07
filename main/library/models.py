from django.db import models
import os

class Book(models.Model):
    name = models.CharField(max_length=255, blank=True)  # Make name optional
    pdf = models.FileField(upload_to='books_pdfs/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.name and self.pdf:
            # Automatically set name from PDF filename (without extension)
            self.name = os.path.splitext(self.pdf.name)[0]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name or "Unnamed Book"
