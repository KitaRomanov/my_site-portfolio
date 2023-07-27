from django.db import models


class WordFile(models.Model):
    file = models.FileField()