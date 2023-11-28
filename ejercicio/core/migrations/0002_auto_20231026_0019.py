# Generated by Django 3.0.7 on 2023-10-26 03:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='tipo_empresa',
            field=models.CharField(default='valor_por_defecto', max_length=255),
        ),
        migrations.AlterField(
            model_name='checklist',
            name='visita',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Visita'),
        ),
    ]
