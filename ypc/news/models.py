from django.db import models
from django.utils import timezone
from django.conf import settings
import os
import shutil

def user_directory_path(instance, filename):
	return 'news/{}/{}'.format(instance.id, filename)

class News(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    description = models.TextField(null=True)
    text = models.TextField()
    cover_image = models.ImageField(null=True, upload_to=user_directory_path)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    attachment = models.FileField(null=True, upload_to=user_directory_path)

    @property
    def filename(self):
        return os.path.basename(self.attachment.name);

    def save(self, *args, **kwargs):
        if self.id is None:
            temp_cover_image = self.cover_image
            temp_attachment = self.attachment
            self.cover_image = None
            self.attachment = None
            super().save(*args, **kwargs)

            self.cover_image = temp_cover_image
            self.attachment = temp_attachment
        super().save(*args, **kwargs)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def delete(self, *args, **kwargs):
        shutil.rmtree(os.path.join(settings.MEDIA_ROOT, "news/{}".format(self.id)))
        # os.remove(os.path.join(settings.MEDIA_ROOT, "sssss/{}".format(self.id)))
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title
