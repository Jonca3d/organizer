from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField('Категория', max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Bookmark(models.Model):
    title = models.CharField('Закладка', max_length=500)
    description = models.TextField('Описание',)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    status = models.BooleanField(default=True, null=True)
    published = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Закладка'
        verbose_name_plural = 'Закладки'

