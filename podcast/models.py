from django.db import models
from django.contrib import admin
# Create your models here.


class Document(models.Model):
    uploadedFile = models.FileField(upload_to="Uploaded_Files/")
    dateTimeOfUpload = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'dateTimeOfUpload')
