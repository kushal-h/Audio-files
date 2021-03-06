# Generated by Django 3.1.1 on 2021-04-28 13:40

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('duration', models.PositiveIntegerField()),
                ('uploaded_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Audiobook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('narrator', models.CharField(max_length=100)),
                ('duration', models.PositiveIntegerField()),
                ('uploaded_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('duration', models.PositiveIntegerField()),
                ('uploaded_time', models.DateTimeField(auto_now_add=True)),
                ('host', models.CharField(max_length=100)),
                ('participants', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), size=10)),
            ],
        ),
    ]
