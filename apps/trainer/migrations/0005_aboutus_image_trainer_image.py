# Generated by Django 5.0.3 on 2024-06-23 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0004_remove_trainer_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='about_us/', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='trainer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='trainers/', verbose_name='Изображение'),
        ),
    ]
