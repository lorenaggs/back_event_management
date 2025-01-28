# Generated by Django 5.1.4 on 2025-01-01 22:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ubicacion',
            name='coordenadas',
        ),
        migrations.AddField(
            model_name='ubicacion',
            name='latitud',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=9),
        ),
        migrations.AddField(
            model_name='ubicacion',
            name='longitud',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='numero_telefono',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{9,15}$', 'Número de teléfono inválido.')]),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='saludo',
            field=models.CharField(blank=True, choices=[('Sr.', 'Sr.'), ('Sra.', 'Sra.'), ('Dr.', 'Dr.')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='titulo',
            field=models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
        migrations.AlterField(
            model_name='evento',
            name='zona_horaria',
            field=models.CharField(choices=[('UTC-5', 'UTC-5'), ('UTC+0', 'UTC+0'), ('UTC+5', 'UTC+5')], default='UTC+0', max_length=50),
        ),
    ]
