from django.db import models

# Create your models here.

class Inventory(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def _str_(self):
        return self.name