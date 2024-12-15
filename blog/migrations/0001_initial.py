# Generated by Django 5.1.4 on 2024-12-15 16:35

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, null=True, upload_to='post_images/')),
            ],
        ),
    ]
