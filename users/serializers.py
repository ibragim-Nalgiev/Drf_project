from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from habits.serializers import HabitSerializer
from users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'phone', 'telegram', 'avatar', 'last_login')


class CustomUserDetailSerializer(serializers.ModelSerializer):
    user_habits = HabitSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'phone', 'telegram', 'avatar', 'last_login', 'user_habits')


class CustomUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = CustomUser.objects.create(**validated_data)
        instance.is_active = True

        if password is not None:
            new_pwd = make_password(password)
            instance.set_password(new_pwd)
        instance.save()

        return instance