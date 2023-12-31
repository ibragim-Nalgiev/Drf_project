# Generated by Django 4.2.3 on 2023-08-30 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='habit_name')),
                ('action', models.TextField(blank=True, null=True, verbose_name='action_description')),
                ('action_time', models.TimeField(verbose_name='action_time')),
                ('action_place', models.CharField(max_length=50, verbose_name='action_place')),
                ('duration', models.DurationField(verbose_name='habit_duration')),
                ('regularity', models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly')], default='daily', max_length=7, verbose_name='habit_regularity')),
                ('days_of_week', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('1', 'Every Monday'), ('2', 'Every Tuesday'), ('3', 'Every Wednesday'), ('4', 'Every Thursday'), ('5', 'Every Friday'), ('6', 'Every Saturday'), ('7', 'Every Sunday')], max_length=23, null=True, verbose_name='days_of_week')),
                ('is_public', models.BooleanField(default=False, verbose_name='is_habit_public')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_habits', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Основная привычка',
                'verbose_name_plural': 'Основные привычки',
            },
        ),
        migrations.CreateModel(
            name='SupportHabit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='support_habit_name')),
                ('action', models.TextField(blank=True, null=True, verbose_name='support_action_description')),
                ('action_time', models.TimeField(blank=True, null=True, verbose_name='support_action_time')),
                ('action_place', models.CharField(blank=True, max_length=50, null=True, verbose_name='support_action_place')),
                ('duration', models.DurationField(blank=True, null=True, verbose_name='support_habit_duration')),
                ('is_public', models.BooleanField(default=False, verbose_name='is_support_habit_public')),
                ('main_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='support_habit', to='habits.habit', verbose_name='main_habit')),
            ],
            options={
                'verbose_name': 'Вспомогательная привычка',
                'verbose_name_plural': 'Вспомогательные привычки',
            },
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='reward_name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='reward_description')),
                ('resources', models.CharField(blank=True, null=True, verbose_name='needed_resources')),
                ('main_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='habit_reward', to='habits.habit', verbose_name='habit_reward')),
            ],
        ),
    ]
