# Generated by Django 3.0.5 on 2020-04-20 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulate_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image_url',
            field=models.FileField(upload_to='articulate/media'),
        ),
    ]
