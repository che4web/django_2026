from django.db import models
import hashlib
import base64

# Create your models here.


class ShortUrl(models.Model):
    order = models.IntegerField(null=True, blank=True)
    source_url = models.TextField(verbose_name="Исходный url")
    short_url = models.TextField(verbose_name="Краткий url")

    def gen_short_url(self):
        short_url = hashlib.sha256(self.source_url.encode()).digest()
        short_url = base64.urlsafe_b64encode(short_url).decode()
        short_url = short_url[:6]
        self.short_url = short_url

    class Meta:
        verbose_name = "Коротик урл"
        verbose_name_plural = "Коротике урлы"
