# Generated by Django 3.0.7 on 2023-11-26 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20231124_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='notificacion_enviada',
            field=models.BooleanField(default=False),
        ),
    ]