from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from habits.models.reward import Reward


class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = '__all__'


class RewardCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = '__all__'

    def create(self, validated_data):
        habit = validated_data.get('main_habit')
        if not habit:
            raise ValidationError(
                {"result":
                     "For a separate Reward object creation you have to specify the 'main_habit' filed value. "
                 }
            )
        if habit.support_habit.all().exists():
            raise ValidationError({
                "result": 'This habit already has an auxiliary habit! '
                          'You can assign either a reward or an auxiliary habit'})
        return super().create(validated_data)


class RewardShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = ('id', 'name',)
