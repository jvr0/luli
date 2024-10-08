# Generated by Django 5.0.7 on 2024-08-21 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0003_rename_asistentes_registro_asistentes_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registro',
            old_name='Asistentes',
            new_name='Edad',
        ),
        migrations.AddField(
            model_name='registro',
            name='Notas',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registro',
            name='Imágen',
            field=models.ImageField(upload_to='Registro', verbose_name='Subí tu foto preferida conmigo para el mural'),
        ),
    ]
