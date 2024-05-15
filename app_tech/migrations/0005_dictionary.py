# Generated by Django 5.0.6 on 2024-05-15 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tech', '0004_building_electronic_standard_connection'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard_number', models.IntegerField()),
                ('language_code', models.CharField(max_length=15)),
                ('language_ru', models.CharField(max_length=250)),
                ('language_uz', models.CharField(max_length=250)),
                ('language_turk', models.CharField(max_length=250)),
                ('language_en', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Dictionary',
                'db_table': 'dictionary',
            },
        ),
    ]