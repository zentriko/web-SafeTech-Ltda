# Generated by Django 3.0.7 on 2023-10-26 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id_administrador', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('usuario', models.CharField(max_length=20, unique=True)),
                ('contrasena', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'administrador',
            },
        ),
        migrations.CreateModel(
            name='Asesoria',
            fields=[
                ('id_asesoria', models.AutoField(primary_key=True, serialize=False)),
                ('detalle', models.CharField(max_length=50, null=True)),
                ('fecha_inicio', models.DateField(blank=True, null=True)),
                ('tipo_asesoria', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'asesoria',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('tipo_empresa', models.CharField(max_length=50, null=True)),
                ('correo', models.CharField(max_length=128)),
                ('usuario', models.CharField(max_length=20, null=True, unique=True)),
                ('contrasena', models.CharField(max_length=20)),
                ('fecha_registro', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cliente',
            },
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id_contrato', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_inicio', models.DateField()),
                ('fecha_termino', models.DateField()),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Cliente')),
            ],
            options={
                'db_table': 'contrato',
            },
        ),
        migrations.CreateModel(
            name='Profesional',
            fields=[
                ('id_pro', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('especialidad', models.CharField(max_length=100)),
                ('usuario', models.CharField(max_length=20, unique=True)),
                ('contrasena', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'profesional',
            },
        ),
        migrations.CreateModel(
            name='Visita',
            fields=[
                ('id_visita', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_visita', models.DateField(null=True)),
                ('resultado', models.CharField(max_length=499, null=True)),
                ('asesoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Asesoria')),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Cliente')),
                ('profesional', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Profesional')),
            ],
            options={
                'db_table': 'visita',
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id_servicio', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_servicio', models.CharField(max_length=50)),
                ('fecha_inicio', models.DateField()),
                ('fecha_termino', models.DateField()),
                ('costo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('administrador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Administrador')),
                ('contrato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Contrato')),
            ],
            options={
                'db_table': 'servicio',
            },
        ),
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id_reporte', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.IntegerField()),
                ('titulo', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=499)),
                ('fecha_creacion', models.DateField()),
                ('administrador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Administrador')),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Cliente')),
            ],
            options={
                'db_table': 'reporte',
            },
        ),
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('id_checklist', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=500)),
                ('tipo_empresa', models.CharField(max_length=30, null=True)),
                ('ruta_documento', models.FileField(upload_to='documentos/')),
                ('visita', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Visita')),
            ],
            options={
                'db_table': 'checklist',
            },
        ),
        migrations.CreateModel(
            name='Capacitacion',
            fields=[
                ('id_capacitacion', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_cap', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('asistentes', models.CharField(max_length=50)),
                ('material', models.CharField(max_length=500)),
                ('asesoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Asesoria')),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Cliente')),
                ('profesional', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Profesional')),
            ],
            options={
                'db_table': 'capacitacion',
            },
        ),
        migrations.CreateModel(
            name='Asesoriaprofesional',
            fields=[
                ('id_asesoriapro', models.AutoField(primary_key=True, serialize=False)),
                ('detalle', models.CharField(max_length=50, null=True)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('prioridad', models.CharField(max_length=15, null=True)),
                ('tipo_asesoria', models.CharField(max_length=50)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Cliente')),
                ('profesional', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Profesional')),
            ],
            options={
                'db_table': 'asesoriaprofesional',
            },
        ),
        migrations.AddField(
            model_name='asesoria',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Cliente'),
        ),
        migrations.AddField(
            model_name='asesoria',
            name='profesional',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Profesional'),
        ),
        migrations.AddField(
            model_name='asesoria',
            name='reporte',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Reporte'),
        ),
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id_actividad', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(max_length=20)),
                ('nombre_act', models.CharField(max_length=20)),
                ('fecha', models.DateField()),
                ('administrador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Administrador')),
                ('checklist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Checklist')),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Cliente')),
                ('profesional', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Profesional')),
            ],
            options={
                'db_table': 'actividad',
            },
        ),
    ]