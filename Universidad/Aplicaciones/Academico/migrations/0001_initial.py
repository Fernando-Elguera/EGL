# Generated by Django 3.2.8 on 2021-11-30 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('num', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('edificio', models.CharField(max_length=2)),
                ('fecharegistrada', models.CharField(max_length=20)),
                ('numerodeparte', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('fecha', models.CharField(max_length=50)),
                ('solicitud', models.CharField(max_length=50)),
            ],
        ),
    ]
