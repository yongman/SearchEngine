from django.db import models

class Results(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=10000)
    url = models.URLField()
