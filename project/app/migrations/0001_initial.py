# Generated by Django 4.1 on 2022-08-25 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_file', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Texts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_text', models.CharField(max_length=40)),
                ('input_radio', models.CharField(max_length=20)),
                ('input_select', models.CharField(max_length=20)),
                ('input_textarea', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
