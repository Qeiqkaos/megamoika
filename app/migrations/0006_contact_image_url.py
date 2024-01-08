# Generated by Django 4.2.2 on 2024-01-07 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_advantage_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='image_url',
            field=models.URLField(default='default-image.jpg', help_text="URL of the Contact's image"),
        ),
    ]