# Generated by Django 5.0.7 on 2024-08-03 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_url',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=1, upload_to='images/blogs/'),
            preserve_default=False,
        ),
    ]
