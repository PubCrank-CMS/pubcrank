from django.db import models

class Page(models.Model):
  path = models.CharField(max_length=255, primary_key=True)
