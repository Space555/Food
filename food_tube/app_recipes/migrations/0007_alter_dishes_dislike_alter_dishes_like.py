# Generated by Django 4.2.7 on 2023-11-16 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_recipes', '0006_alter_dishes_dislike_alter_dishes_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishes',
            name='dislike',
            field=models.PositiveIntegerField(default=0, verbose_name='Дизлайки'),
        ),
        migrations.AlterField(
            model_name='dishes',
            name='like',
            field=models.PositiveIntegerField(default=0, verbose_name='Лайки'),
        ),
    ]
