# Generated by Django 4.2.5 on 2023-09-06 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
    ]