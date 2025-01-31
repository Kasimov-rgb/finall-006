from django.db import models
from django.contrib.auth import get_user_model
from apps.trainer.models import Trainer

User = get_user_model()


class Reviews(models.Model):
    trainer = models.ForeignKey(
        Trainer,
        on_delete=models.CASCADE,
        verbose_name="Тренер",
        related_name="reviews"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
    )
    text = models.CharField(
        max_length=500,
        verbose_name="Текст",
    )
    image = models.ImageField(
        upload_to='review_images/',
        null=True,
        blank=True,
        verbose_name="Изображение"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время добавления",
    )

    def __str__(self):
        return f"{self.user} - {self.trainer}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
