from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from datetime import datetime


class Dishes(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000, verbose_name='Блюдо', db_index=True, null=True)
    descr = models.TextField(verbose_name='Приготовление', null=True, blank=True)
    cat_id = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Каткгория', null=True)
    created = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateField(auto_now=True, verbose_name='Дата обновления')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d', verbose_name='Фото блюда', null=True, blank=True)
    video = models.FileField(upload_to='video/%Y/%m/%d', verbose_name='Видео приготовления', null=True, blank=True)
    like = models.ManyToManyField(User, related_name='liked_dishes', verbose_name='Лайки', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def get_absolute_url(self):
        return reverse('detail_dishes', kwargs={'pk': self.pk})

    def get_upload_url(self):
        if self.photo:
            return self.photo.url
        if self.video:
            return self.video.url

    def like_count(self):
        return self.like.count()

    def descr_len(self):
        if len(self.descr) >= 50:
            return f'{self.descr[:50]} ...'
        else:
            return self.descr


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название категории', null=True, blank=True)
    created = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateField(auto_now=True, verbose_name='Дата обновления')
    pic = models.ImageField(upload_to='bgc/%Y/%m/%d/', verbose_name='Картинка категории', null=True, blank=True)
    slug = models.SlugField(null=True, verbose_name='URL')

    class Meta:
        ordering = ['title']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_category', kwargs={'pk': self.pk})

    def get_upload_url(self):
        return self.pic.url


class StepDishes(models.Model):
    dish = models.ForeignKey(Dishes, on_delete=models.CASCADE, related_name='steps', null=True, blank=True,
                             verbose_name='Блюдо')
    pic = models.ImageField(upload_to='steps/%Y/%m/%d', verbose_name='Фото', blank=True, null=True,)
    desc = models.TextField(verbose_name='Описание шага', blank=True, null=True)

    class Meta:
        verbose_name = 'Шаг'
        verbose_name_plural = 'Шаги'

    def __str__(self):
        return f'Шаги к {self.dish}'

    def get_upload_url(self):
        return self.pic.url


class Comments(models.Model):
    dish_id = models.ForeignKey(Dishes, on_delete=models.CASCADE, related_name='text', verbose_name='Блюдо', null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', null=True, blank=True)
    comment = models.TextField(verbose_name='Комментарий', null=True, blank=True)
    created = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'Комментарий {self.author.username} для {self.dish_id.title}'






