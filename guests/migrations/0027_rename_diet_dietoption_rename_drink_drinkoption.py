# Generated by Django 4.2.16 on 2024-11-09 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0026_fill_drink_data'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Diet',
            new_name='DietOption',
        ),
        migrations.RenameModel(
            old_name='Drink',
            new_name='DrinkOption',
        ),
    ]
