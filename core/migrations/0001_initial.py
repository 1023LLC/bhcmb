# Generated by Django 5.0.1 on 2024-02-05 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('venue', models.CharField(max_length=255)),
                ('image_url', models.URLField()),
                ('directions_url', models.URLField()),
                ('date_time', models.DateTimeField()),
                ('description', models.TextField()),
                ('booking_url', models.URLField()),
            ],
        ),
    ]