# Generated by Django 3.2.19 on 2023-05-17 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productpromo',
            name='name',
        ),
        migrations.AddField(
            model_name='productpromo',
            name='promo',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
    ]