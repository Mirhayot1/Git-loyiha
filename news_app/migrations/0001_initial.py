# Generated by Django 5.1.1 on 2024-09-18 18:54

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('slug', models.SlugField(max_length=300)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='news/images')),
                ('publish_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('DFDraft', 'Draft'), ('PB', 'Published')], default='DFDraft', max_length=7)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_app.category')),
            ],
        ),
    ]
