from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from habits.models.support_habit import SupportHabit


class SupportHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportHabit
        fields = ('id', 'main_habit', 'name', 'action', 'action_time', 'action_place', 'duration', 'is_public')


class SupportHabitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportHabit
        fields = '__all__'

    def create(self, validated_data):
        habit = validated_data.get('main_habit')
        if not habit:
            raise ValidationError(
                {"result":
                     "For a separate SupportHabit object creation you have to specify the 'main_habit' filed value."
                 }
            )
        if habit.habit_reward.all().exists():
            raise ValidationError({
                "result": 'This habit already has a reward! You can assign either a reward or a support habit'})
        return super().create(validated_data)


class SupportHabitShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportHabit
        fields = ('name', 'action',)