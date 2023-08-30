from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import SerializerMethodField

from habits.models.habit import Habit
from habits.models.reward import Reward
from habits.models.support_habit import SupportHabit
from habits.serializers import RewardShortSerializer, RewardCreateSerializer
from habits.serializers.support_habit_serializers import SupportHabitShortSerializer, SupportHabitCreateSerializer
from habits.validators import IsTooLong


class HabitSerializer(serializers.ModelSerializer):
    has_auxiliary_habits = SerializerMethodField()
    support_habit = SupportHabitShortSerializer(read_only=True, many=True)
    has_reward = SerializerMethodField()
    habit_reward = RewardShortSerializer(read_only=True, many=True)

    class Meta:
        model = Habit
        fields = ('id', 'name', 'user', 'action', 'action_time', 'action_place', 'duration', 'regularity', 'is_public',
                  'has_support_habits', 'support_habit', 'has_reward', 'habit_reward',)

    def get_has_auxiliary_habits(self, habit):
        if SupportHabit.objects.filter(main_habit=habit).exists():
            return True
        return False

    def get_has_reward(self, habit):
        if Reward.objects.filter(main_habit=habit).exists():
            return True
        return False


class HabitCreateSerializer(serializers.ModelSerializer):
    habit_reward = RewardCreateSerializer(many=True, required=False)
    support_habit = SupportHabitCreateSerializer(many=True, required=False)
    days_of_week = serializers.ListField(required=False)

    class Meta:
        model = Habit
        fields = (
            'id', 'name', 'user', 'action', 'action_time', 'action_place', 'duration', 'regularity', 'is_public',
            'habit_reward', 'support_habit', 'days_of_week')
        validators = [IsTooLong(field='duration')]

    def create(self, validated_data):

        habit_reward_data = validated_data.pop('habit_reward', [])
        support_habit_data = validated_data.pop('support_habit', [])
        main_habit = Habit.objects.create(**validated_data)

        if habit_reward_data and support_habit_data:
            raise ValidationError('You can assign either a reward or an auxiliary habit')

        for r in habit_reward_data:
            Reward.objects.create(main_habit=main_habit, **r)

        for h in support_habit_data:
            SupportHabit.objects.create(main_habit=main_habit, **h)

        return main_habit
