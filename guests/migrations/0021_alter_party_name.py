# Generated by Django 4.2.16 on 2024-11-09 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0020_alter_guest_email_alter_guest_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='name',
            field=models.CharField(max_length=128),
        ),
    ]