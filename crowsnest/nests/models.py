from django.db import models


class Cluster(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=256)
    secret_key = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.name

