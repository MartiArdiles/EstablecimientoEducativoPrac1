# Generated by Django 3.2.9 on 2021-12-11 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0005_auto_20211209_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docente',
            name='materia',
            field=models.CharField(blank=True, choices=[('0', 'Programación 2'), ('1', 'Práctica 1'), ('2', 'Matemática Aplicada'), ('3', 'Modelado de Sistemas'), ('4', 'Sistemas Operativos'), ('5', 'Base de Datos')], max_length=50, null=True, unique=True, verbose_name='Materia'),
        ),
    ]
