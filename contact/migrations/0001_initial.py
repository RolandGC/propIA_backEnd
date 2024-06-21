# Generated by Django 5.0.5 on 2024-06-19 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('celular', models.CharField(max_length=15)),
                ('tipo_solicitud', models.CharField(max_length=20)),
                ('mensaje', models.TextField(max_length=300)),
                ('ciudad', models.CharField(max_length=100)),
                ('provincia', models.CharField(max_length=100)),
                ('codigo_postal', models.CharField(max_length=100)),
            ],
        ),
    ]