from django.db import models

from habits.models.habit import Habit
from users.models import NULLABLE


class Reward(models.Model):
    main_habit = models.ForeignKey(Habit, on_delete=models.SET_NULL, verbose_name='habit_reward',
                                   related_name='habit_reward', **NULLABLE)
    name = models.CharField(verbose_name='reward_name', max_length=50, unique=True)
    description = models.TextField(verbose_name='reward_description', **NULLABLE)
    resources = models.CharField(verbose_name='needed_resources', **NULLABLE)