# Generated by Django 4.2.16 on 2024-11-09 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0019_fill_my_model_with_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='email',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='guest',
            name='first_name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='guest',
            name='last_name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]