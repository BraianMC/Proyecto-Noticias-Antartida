# Generated by Django 2.2.24 on 2021-11-25 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adjunto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=None, max_length=50)),
                ('formato', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Configuracion_Fuente_Informacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buscar_Titulo', models.CharField(blank=None, max_length=200)),
                ('buscar_Contenido', models.CharField(blank=None, max_length=200)),
                ('buscar_Imagenes', models.CharField(blank=None, max_length=200)),
                ('buscar_links', models.CharField(blank=None, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Contenido_Original',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_acceso', models.DateField(blank=None, default=None)),
                ('contenido', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Fuente_Informacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=None, max_length=100)),
                ('URL', models.URLField(blank=None)),
                ('tipo', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
                ('idConfiguracion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_RDNA.Configuracion_Fuente_Informacion')),
                ('idContenido_Original', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_RDNA.Contenido_Original')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=None, max_length=30)),
                ('contraseña', models.CharField(blank=None, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=None, max_length=50)),
                ('idioma', models.CharField(blank=None, max_length=50)),
                ('idFuente_Informacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_RDNA.Fuente_Informacion')),
            ],
        ),
        migrations.CreateModel(
            name='Contenido_Procesado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=None, max_length=100)),
                ('fecha_Creacion', models.DateField(blank=None, default=None)),
                ('contenido', models.TextField()),
                ('anotacion', models.TextField()),
                ('idAdjunto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_RDNA.Adjunto')),
                ('idContenido_Original', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_RDNA.Contenido_Original')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('concepto', models.CharField(blank=None, max_length=100)),
                ('contenidos_Procesados_Relacionados', models.ManyToManyField(to='App_RDNA.Contenido_Procesado')),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_RDNA.Usuario')),
            ],
        ),
    ]