# Generated by Django 3.0.5 on 2020-04-22 09:59

import articulate_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulate_app', '0006_auto_20200422_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image_url',
            field=models.FileField(help_text='Maximum file size allowed is 150kb', unique=True, upload_to='uploaded_images/', validators=[articulate_app.models.validate_image]),
        ),
        migrations.AlterField(
            model_name='article',
            name='rating',
            field=models.FloatField(validators=[articulate_app.models.validate_rating]),
        ),
    ]
