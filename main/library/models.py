from django.db import models
import os
from pdf2image import convert_from_path
from PIL import Image
import io
from django.core.files.base import ContentFile
import logging

logger = logging.getLogger(__name__)

class Book(models.Model):
    name = models.CharField(max_length=255, blank=True)
    pdf = models.FileField(upload_to='books_pdfs/')
    first_page_image = models.ImageField(upload_to='books_first_pages/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        is_new = self.pk is None

        if not self.name and self.pdf:
            self.name = os.path.splitext(self.pdf.name)[0]

        super().save(*args, **kwargs)

        if is_new and self.pdf and not self.first_page_image:
            try:
                pdf_path = self.pdf.path
                images = convert_from_path(pdf_path, first_page=1, last_page=1)

                if images:
                    buffer = io.BytesIO()
                    images[0].save(buffer, format="PNG")
                    image_file = ContentFile(buffer.getvalue())

                    image_filename = f"{os.path.splitext(os.path.basename(self.pdf.name))[0]}_first_page.png"
                    self.first_page_image.save(image_filename, image_file, save=True)

            except Exception as e:
                logger.error("❌ Error generating first page image from PDF", exc_info=True)

    def __str__(self):
        return self.name or "Unnamed Book"
