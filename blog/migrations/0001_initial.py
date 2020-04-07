# Generated by Django 3.0.5 on 2020-04-06 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Título')),
                ('text', models.TextField(verbose_name='Texto')),
                ('excerpt', models.CharField(blank=True, max_length=120, verbose_name='Resumen')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Feha y hora de creación')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='fecha y hora de actualización')),
            ],
            options={
                'verbose_name': 'Publicación',
                'verbose_name_plural': 'Publicaciones',
            },
        ),
    ]