# Generated by Django 5.0.3 on 2024-05-25 05:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0015_remove_orden_precio_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mesa',
            name='num_orden',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Menu.orden'),
        ),
    ]