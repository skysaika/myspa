from django.db import models

from users.models import NULLABLE


class Course(models.Model):
    """Модель курса"""
    title = models.CharField(max_length=255, verbose_name='название')
    preview = models.ImageField(upload_to='courses/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    """Модель урока"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')
    name = models.CharField(max_length=255, verbose_name='название')
    preview = models.ImageField(upload_to='lessons/', verbose_name='превью', **NULLABLE)
    url_video = models.URLField(verbose_name='ссылка на видео', **NULLABLE)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

