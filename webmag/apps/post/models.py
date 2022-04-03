
from django.db import models
from ckeditor.fields import RichTextField

from ..users.models import User


class PostCategory(models.Model):
    """ Категория поста"""

    title = models.CharField(max_length=225, unique=True, verbose_name='Заголовок')

    class Meta:
        verbose_name_plural = 'Категории публикаций'
        verbose_name = 'Категория публикации'

    def __str__(self):
        return self.title


class PostTag(models.Model):
    """ Тэги для постов """

    title = models.CharField(max_length=255, unique=True, verbose_name='Заголовок')

    class Meta:
        verbose_name_plural = 'Тэги'
        verbose_name = 'Тэг'

    def __str__(self):
        return self.title

class PostManager(models.Manager):

    def all_random_order(self):
        """ возвращает отсортированный в рандомном порядке queryset """
        return self.order_by('?').all()

class Post(models.Model):
    """ Публикация для постов """

    title = models.CharField(max_length=200, verbose_name='Заголовок поста')
    image = models.ImageField(verbose_name='Изображение')
    text = RichTextField(verbose_name='Содержание')
    category = models.ForeignKey(to=PostCategory, related_name='posts', on_delete=models.CASCADE)
    tag = models.ManyToManyField(to=PostTag, related_name='posts')
    author = models.ForeignKey(User, related_name='post', on_delete=models.CASCADE)
    create_at = models.DateField(auto_now_add=True)

    objects = PostManager()


class PostComment(models.Model):
    """ Модель для комментария"""


    text = models.TextField(verbose_name='Текст')
    user_name = models.CharField(max_length=100, verbose_name='Имя пользователя', blank=False)
    user_email = models.EmailField(unique=True, blank=False)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE,
                                related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Комментарии публикаций'
        verbose_name = 'Комментарий публикации'

    def __str__(self):
        return f'Комментарий публикации с id:{self.article_id}'
