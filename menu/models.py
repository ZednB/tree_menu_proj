from django.db import models
from django.urls import reverse

NULLABLE = {'blank': True, 'null': True}


class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Меню')

    def __str__(self):
        return f"{self.name}"


class MenuItem(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    url = models.CharField(max_length=200, **NULLABLE, verbose_name='Ссылка')
    named_url = models.CharField(max_length=200, **NULLABLE, verbose_name='Название ссылки')
    parent = models.ForeignKey('self', **NULLABLE, related_name='children', on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    def get_url(self):
        if self.url:
            return self.url
        elif self.named_url:
            return reverse(self.named_url)
        return '#'
