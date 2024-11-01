from django.db import models
from django.db.models import CASCADE


class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название тега', unique=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )
    tags = models.ManyToManyField(Tag, related_name='articles', through='Scope', verbose_name='Теги')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes')
    is_main = models.BooleanField(default=False, verbose_name='Основной тег')

    class Meta:
        verbose_name = 'Tematika statii'

    #    unique_together = ('article', 'is_main')

    def __str__(self):
        return f"{self.article} - {self.tag}"
