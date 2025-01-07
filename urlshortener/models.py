from django.db import models
from utils.url_services import shortener_url_generator

# Create your models here.


class UrlShortener(models.Model):
    original_url = models.URLField(max_length=200)
    short_url = models.CharField(max_length=5, blank=True, null=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    times_used = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "UrlShortener"
        verbose_name_plural = "UrlShorteners"
        ordering = ["-created"]

    def __str__(self):
        return f"{self.original_url} converted to {self.short_url}"

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = shortener_url_generator(self)
        return super().save(*args, **kwargs)
