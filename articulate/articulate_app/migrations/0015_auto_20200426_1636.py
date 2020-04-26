# Generated by Django 3.0.5 on 2020-04-26 11:06

import articulate_app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulate_app', '0014_auto_20200423_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image_url',
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.FileField(help_text='Maximum file size allowed is 80kb', null=True, unique=True, upload_to='', validators=[articulate_app.validators.validate_image], verbose_name='Movie Poster'),
        ),
    ]
