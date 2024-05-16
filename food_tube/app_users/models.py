from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, db_index=True, verbose_name='Пользователь', on_delete=models.CASCADE, null=True,
                                related_name='profile')
    city = models.CharField(max_length=200, verbose_name='Город', null=True, blank=True)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', verbose_name='Фото профиля', null=True, blank=True)
    dish_count = models.PositiveIntegerField(default=0, verbose_name='Счетчик блюд')

    def __str__(self):
        return f'Профиль {self.user.username}'

    def get_absolute_url(self):
        return reverse('profile_d', kwargs={'pk': self.pk})

    def get_upload_url(self):
        return self.avatar.url

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
