# Generated by Django 5.0.3 on 2024-03-16 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, upload_to='covers/'),
        ),
    ]
