from django.db import models

# Create your models here.


class ShortUrl(models.Model):
    order = models.IntegerField(null=True, blank=True)
    source_url = models.TextField(verbose_name="Исходный url")
    short_url = models.TextField(verbose_name="Краткий url")

    class Meta:
        verbose_name = "Коротик урл"
        verbose_name_plural = "Коротике урлы"
