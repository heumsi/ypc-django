from django.db import models
from django.utils import timezone
import os

class News(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    description = models.TextField(null=True)
    text = models.TextField()
    cover_image = models.ImageField(null=True, upload_to="news/")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    attachment = models.FileField(null=True, upload_to="news/")

    @property
    def filename(self):
        return os.path.basename(self.attachment.name);

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
