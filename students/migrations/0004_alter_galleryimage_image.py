# Generated by Django 5.0.4 on 2024-05-25 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_portfolio_gallery_alter_project_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='gallery/'),
        ),
    ]
