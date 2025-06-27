from django.db import models

class Test(models.Model):
    title = models.CharField(max_length=20)
    file = models.FileField(upload_to="timur")