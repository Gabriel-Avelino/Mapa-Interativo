# Generated by Django 5.1.2 on 2024-10-21 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=256, null=True)),
                ('segunda', models.TimeField(blank=True, null=True)),
                ('terca', models.TimeField(blank=True, null=True)),
                ('quarta', models.TimeField(blank=True, null=True)),
                ('quinta', models.TimeField(blank=True, null=True)),
                ('sexta', models.TimeField(blank=True, null=True)),
                ('sabado', models.TimeField(blank=True, null=True)),
                ('domingo', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Search',
        ),
    ]
