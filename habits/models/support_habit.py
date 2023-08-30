from django.db import models

from habits.models.habit import Habit
from users.models import NULLABLE


class SupportHabit(models.Model):
    main_habit = models.ForeignKey(Habit, verbose_name='main_habit', related_name='support_habit',
                                   on_delete=models.SET_NULL, **NULLABLE)
    name = models.CharField(verbose_name='support_habit_name', max_length=50, unique=True)
    action = models.TextField(verbose_name='support_action_description', **NULLABLE)
    action_time = models.TimeField(verbose_name='support_action_time', **NULLABLE)
    action_place = models.CharField(verbose_name='support_action_place', max_length=50, **NULLABLE)
    duration = models.DurationField(verbose_name='support_habit_duration', **NULLABLE)
    is_public = models.BooleanField(default=False, verbose_name='is_support_habit_public')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Вспомогательная привычка'
        verbose_name_plural = 'Вспомогательные привычки'
