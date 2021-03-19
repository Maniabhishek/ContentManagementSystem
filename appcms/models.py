from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
# from appcms.api.validators import validate_file_extension
from django.core.validators import FileExtensionValidator
# Create your models here.


class Content(models.Model):
    CATEGORY = (
        ('Politics', 'Politics'),
        ('Sports', 'Sports'),
        ('Entertainment', 'Entertainment'),
        ('Science', 'Science'),
    )
    date_posted = models.DateTimeField(
        default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=30, null=True, blank=True)
    body = models.TextField(max_length=300, null=True, blank=True)
    summary = models.CharField(max_length=60, null=True, blank=True)
    category = models.CharField(
        max_length=30, null=True, choices=CATEGORY, blank=True)
    pdf = models.FileField(upload_to='content/pdfs/', null=True,
                           blank=True, validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    def get_absolute_url(self):
        return reverse('contentDetail', kwargs={'pk': self.pk})
