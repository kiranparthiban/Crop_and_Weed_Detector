# Generated by Django 5.1.2 on 2025-02-04 15:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_data', models.ImageField(blank=True, null=True, upload_to='uploaded_images/')),
                ('processed_image', models.ImageField(blank=True, null=True, upload_to='processed_images/')),
                ('model_chosen', models.CharField(default='default_model', max_length=100)),
                ('summary', models.TextField(blank=True, default='Detected species placeholder', null=True)),
                ('crop_name', models.CharField(default='Unknown Crop', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
