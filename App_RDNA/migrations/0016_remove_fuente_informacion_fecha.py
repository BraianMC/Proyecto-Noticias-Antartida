# Generated by Django 2.2.24 on 2021-12-18 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_RDNA', '0015_fuente_informacion_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fuente_informacion',
            name='fecha',
        ),
    ]
