# Generated by Django 3.0.5 on 2020-04-20 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulate_app', '0002_auto_20200420_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='rating',
            field=models.CharField(choices=[('poor', 'Poor'), ('average', 'Average'), ('good', 'Good'), ('vgood', 'Very Good'), ('excellent', 'Excellent')], max_length=10),
        ),
    ]
