# Generated by Django 4.2.16 on 2024-11-09 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0024_alter_party_invitation_opened'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=128)),
            ],
        ),
        migrations.RemoveField(
            model_name='diet',
            name='guests',
        ),
        migrations.AddField(
            model_name='guest',
            name='diets',
            field=models.ManyToManyField(blank=True, to='guests.diet'),
        ),
        migrations.DeleteModel(
            name='Drinks',
        ),
        migrations.AddField(
            model_name='guest',
            name='drinks',
            field=models.ManyToManyField(blank=True, to='guests.drink'),
        ),
    ]