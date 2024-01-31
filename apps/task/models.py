from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Название"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    completed = models.BooleanField(
        default = False,
        verbose_name="Статус описание"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="Задача"
        verbose_name_plural="Задачи"