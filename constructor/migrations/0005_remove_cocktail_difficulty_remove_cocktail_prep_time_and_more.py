# Generated by Django 4.2.5 on 2023-09-16 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0004_rename_recipe_id_cocktailingredient_cocktail_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cocktail',
            name='difficulty',
        ),
        migrations.RemoveField(
            model_name='cocktail',
            name='prep_time',
        ),
        migrations.RemoveField(
            model_name='cocktail',
            name='rating',
        ),
    ]