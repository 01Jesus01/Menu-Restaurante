# Generated by Django 5.0.2 on 2024-05-23 06:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Menu", "0010_mesa_numero_mesa"),
    ]

    operations = [
        migrations.AddField(
            model_name="orden",
            name="estado",
            field=models.BooleanField(default=True),
        ),
    ]
