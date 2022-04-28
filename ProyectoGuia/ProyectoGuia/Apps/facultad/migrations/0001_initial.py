# Generated by Django 4.0.3 on 2022-04-20 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('nombreCorto', models.CharField(max_length=10, unique=True, verbose_name='NombreCorto')),
                ('activo', models.BooleanField(default=True, verbose_name='FacultadActiva')),
            ],
            options={
                'verbose_name': 'Facultad',
                'verbose_name_plural': 'Nuestras Facultades',
                'ordering': ['nombre'],
                'unique_together': {('nombre', 'nombreCorto')},
            },
        ),
    ]
