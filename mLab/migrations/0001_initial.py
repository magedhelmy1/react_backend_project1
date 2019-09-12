# Generated by Django 2.2.5 on 2019-09-09 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mlab',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('mLab_name', models.CharField(max_length=255)),
                ('mLab_city_location', models.CharField(max_length=255)),
                ('mLab_department', models.CharField(max_length=255)),
                ('clinical_condition', models.CharField(max_length=255)),
                ('session_videos', models.CharField(max_length=255)),
                ('session_drs', models.CharField(max_length=255)),
            ],
        ),
    ]
