# Generated by Django 5.1.3 on 2024-12-18 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('petName', models.CharField(max_length=255)),
                ('petAge', models.IntegerField()),
                ('petBreed', models.CharField(max_length=255)),
                ('petImage', models.CharField(max_length=500)),
            ],
        ),
    ]
