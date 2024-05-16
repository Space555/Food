# Generated by Django 4.2.7 on 2023-11-05 15:59

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dishes',
            options={'ordering': ['title'], 'verbose_name': 'Блюдо', 'verbose_name_plural': 'Блюда'},
        ),
        migrations.AddField(
            model_name='dishes',
            name='cat_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_recipes.category', verbose_name='Каткгория'),
        ),
        migrations.AddField(
            model_name='dishes',
            name='created',
            field=models.DateField(default=datetime.datetime(2023, 11, 5, 21, 59, 36, 734091), verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='dishes',
            name='descr',
            field=models.TextField(null=True, verbose_name='Приготовление'),
        ),
        migrations.AddField(
            model_name='dishes',
            name='title',
            field=models.CharField(db_index=True, max_length=1000, null=True, verbose_name='Блюдо'),
        ),
        migrations.AddField(
            model_name='dishes',
            name='updated',
            field=models.DateField(auto_now=True, verbose_name='Дата обновления'),
        ),
        migrations.AddField(
            model_name='dishes',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]