from django.contrib import admin


from habits.models import Habit, SupportHabit, Reward


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'name', 'user', 'action', 'action_time', 'action_place', 'duration', 'regularity', 'is_public',)


@admin.register(SupportHabit)
class AuxiliaryHabitAdmin(admin.ModelAdmin):
    list_display = ('pk', 'main_habit', 'name', 'action', 'action_time', 'action_place', 'duration', 'is_public',)


@admin.register(Reward)
class RewardHabitAdmin(admin.ModelAdmin):
    list_display = ('pk', 'main_habit', 'name', 'description', 'resources',)