# Generated by Django 4.1 on 2022-09-15 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=1000)),
                ('price', models.CharField(max_length=80)),
                ('link_img', models.URLField(max_length=1000)),
                ('link_url', models.URLField(max_length=1000)),
                ('origin', models.CharField(max_length=80)),
                ('search', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.search')),
            ],
        ),
    ]
