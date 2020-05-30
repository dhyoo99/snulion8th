from django.db import models
from django.utils import timezone

class Feed(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)
    photo = models.ImageField(blank=True, upload_to='feed_photos')

    def update_date(self):
        self.updated_At = timezone.now()
        self.save()

    def __str__(self):
        return self.title