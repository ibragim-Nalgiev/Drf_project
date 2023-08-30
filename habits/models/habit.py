from django.conf import settings
from django.db import models
from multiselectfield import MultiSelectField
from rest_framework.exceptions import ValidationError

from users.models import NULLABLE


class Habit(models.Model):
    REGULARITY_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
    ]

    DAYS_CHOICES = [
        ('1', "Every Monday"),
        ('2', "Every Tuesday"),
        ('3', "Every Wednesday"),
        ('4', "Every Thursday"),
        ('5', "Every Friday"),
        ('6', "Every Saturday"),
        ('7', "Every Sunday"),
    ]

    name = models.CharField(verbose_name='habit_name', unique=True, max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='user', on_delete=models.SET_NULL,
                             related_name='user_habits', **NULLABLE)
    action = models.TextField(verbose_name='action_description', **NULLABLE)
    action_time = models.TimeField(verbose_name='action_time')
    action_place = models.CharField(verbose_name='action_place', max_length=50)
    duration = models.DurationField(verbose_name='habit_duration')
    regularity = models.CharField(verbose_name='habit_regularity', choices=REGULARITY_CHOICES, default='daily',
                                  max_length=7)
    days_of_week = MultiSelectField(choices=DAYS_CHOICES, **NULLABLE, verbose_name='days_of_week', max_choices=7,
                                    max_length=23)
    is_public = models.BooleanField(default=False, verbose_name='is_habit_public')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Основная привычка'
        verbose_name_plural = 'Основные привычки'

    def save(self, *args, **kwargs):
        if self.regularity == 'daily' and self.days_of_week:
            raise ValidationError(
                "You have to select 'Weekly' as the regularity mode if you want to specify days of the week!"
            )
        elif self.regularity == 'weekly' and not self.days_of_week:
            raise ValidationError(
                "You have to specify days of the week for the 'Weekly' regularity mode!"
            )
        super().save(*args, **kwargs)