# Generated by Django 5.0.3 on 2024-05-23 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0011_perfil'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]
