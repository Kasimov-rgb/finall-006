# Generated by Django 5.0.3 on 2024-07-09 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0007_rename_image_trainer_for_image_trainer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='for_image_trainer',
        ),
        migrations.AddField(
            model_name='trainer',
            name='image_for_trainer',
            field=models.ImageField(blank=True, null=True, upload_to='trainer_media/'),
        ),
    ]
