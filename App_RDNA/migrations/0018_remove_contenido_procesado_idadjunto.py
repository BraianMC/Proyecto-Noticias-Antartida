# Generated by Django 2.2.24 on 2021-12-19 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_RDNA', '0017_auto_20211218_1645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contenido_procesado',
            name='idAdjunto',
        ),
    ]
