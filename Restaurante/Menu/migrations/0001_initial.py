# Generated by Django 5.0.3 on 2024-05-12 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_platillo', models.CharField(max_length=100)),
                ('Descripcion', models.CharField(max_length=300)),
                ('Precio', models.IntegerField(max_length=20)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes/')),
            ],
        ),
    ]
