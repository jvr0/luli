# Generated by Django 5.0.6 on 2024-07-18 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='asistentes',
            field=models.IntegerField(),
        ),
    ]
