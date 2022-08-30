from django.db import models


# Create your models here.
class Texts(models.Model):
    input_text = models.CharField(max_length=40)
    input_radio = models.CharField(max_length=20)
    input_select = models.CharField(max_length=20)
    input_textarea = models.CharField(max_length=255)
    date = models.DateTimeField()


class Files(models.Model):
    input_file = models.CharField(max_length=255)
    input_filepath = models.CharField(max_length=255)
    date = models.DateTimeField()
