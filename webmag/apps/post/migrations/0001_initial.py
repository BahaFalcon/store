# Generated by Django 3.2 on 2022-03-31 13:50

import ckeditor.fields
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
                ('title', models.CharField(max_length=200, verbose_name='Заголовок поста')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('text', ckeditor.fields.RichTextField(verbose_name='Содержание')),
                ('create_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225, unique=True, verbose_name='Заголовок')),
            ],
            options={
                'verbose_name': 'Категория публикации',
                'verbose_name_plural': 'Категории публикаций',
            },
        ),
        migrations.CreateModel(
            name='PostTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Заголовок')),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
            },
        ),
    ]
