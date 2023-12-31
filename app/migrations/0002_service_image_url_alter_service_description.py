# Generated by Django 4.2.2 on 2024-01-04 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='image_url',
            field=models.URLField(default='default-image.jpg', help_text="URL of the Service's image"),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(help_text="The Service's description.", max_length=50),
        ),
    ]
