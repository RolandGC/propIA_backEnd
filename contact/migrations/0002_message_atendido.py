# Generated by Django 5.0.5 on 2024-06-20 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='atendido',
            field=models.BooleanField(default=False),
        ),
    ]