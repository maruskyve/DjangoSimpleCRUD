# Generated by Django 4.1 on 2022-08-28 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='input_filepath',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]