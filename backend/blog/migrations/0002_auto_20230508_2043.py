# Generated by Django 3.2.19 on 2023-05-08 17:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='created_timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='publication',
            name='image',
            field=models.ImageField(upload_to='publication_images'),
        ),
    ]