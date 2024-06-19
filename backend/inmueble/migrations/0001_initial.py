# Generated by Django 5.0.5 on 2024-06-19 15:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_operation', models.CharField(max_length=20)),
                ('type_property', models.CharField(max_length=50)),
                ('subtype_property', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('dni', models.CharField(max_length=8)),
                ('phone_number', models.CharField(max_length=9)),
                ('adress', models.CharField(max_length=150)),
                ('departamento', models.CharField(max_length=30)),
                ('provincia', models.CharField(max_length=50)),
                ('distrito', models.CharField(max_length=50)),
                ('urbanization', models.CharField(max_length=30)),
                ('area_property', models.DecimalField(decimal_places=3, max_digits=10)),
                ('bedrooms_number', models.CharField(max_length=2)),
                ('garages_number', models.CharField(max_length=2)),
                ('bathrooms_number', models.CharField(max_length=2)),
                ('kitchens_number', models.CharField(max_length=2)),
                ('floors_number', models.CharField(max_length=2)),
                ('type_currency', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=3, max_digits=20)),
                ('description', models.TextField(max_length=800)),
                ('terms_conditions', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ImageProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='property/image')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='inmueble.property')),
            ],
        ),
    ]
