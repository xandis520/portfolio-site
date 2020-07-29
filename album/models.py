from django.db import models
from django.urls import reverse

# Create your models here.


class TrendLineExample(models.Model):
    stock_data = models.TextField()
    step = models.DecimalField(decimal_places=0, max_digits=20)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("album:trend-line-example", kwargs={"id": self.id})