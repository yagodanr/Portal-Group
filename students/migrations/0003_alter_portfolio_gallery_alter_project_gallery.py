# Generated by Django 5.0.3 on 2024-05-22 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_galleryimage_remove_project_image_portfolio_gallery_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='gallery',
            field=models.ManyToManyField(blank=True, to='students.galleryimage'),
        ),
        migrations.AlterField(
            model_name='project',
            name='gallery',
            field=models.ManyToManyField(blank=True, to='students.galleryimage'),
        ),
    ]
