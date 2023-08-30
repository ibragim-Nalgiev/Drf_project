from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit, Reward
from users.models import CustomUser


class RewardTestCases(APITestCase):
    def setUp(self):
        self.user_data = {'email': 'testing@mail.com', 'telegram': '@testing', "password": "12345678"}
        self.user = CustomUser.objects.create(**self.user_data)
        self.client.force_authenticate(user=self.user)
        data = {"name": "New habit", "action_time": "22:00:00",
                "action_place": "Home", "duration": "PT2M", "user": self.user}
        self.main_habit = Habit.objects.create(**data)
        reward_data = {"name": "Test reward", "main_habit": self.main_habit}
        self.reward = Reward.objects.create(**reward_data)

    def test_create_reward(self):
        data = {"name": "New reward", "main_habit": self.main_habit.pk}
        response = self.client.post('http://localhost:8000/habits/rewards/', data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(Reward.objects.all().count(), 2)
        self.assertEquals(
            response.json()['name'], 'New reward')

    def test_list_reward(self):
        response = self.client.get('http://localhost:8000/habits/rewards/')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(Reward.objects.all().count(), 1)
        self.assertEquals(response.json(), {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [
                {'id': self.reward.pk, 'name': 'Test reward', 'description': None, 'resources': None,
                 'main_habit': self.main_habit.pk}
            ]
        })

    def test_update_support_habit(self):
        data = {"name": "New reward", "main_habit": self.main_habit}
        reward = Reward.objects.create(**data)
        params = {"name": "UPDATED reward", "main_habit": self.main_habit.pk}
        response = self.client.put(f'http://localhost:8000/habits/rewards/{reward.pk}/', data=params)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(
            response.json()['name'],
            'UPDATED reward'
        )

    def test_partial_update_support_habit(self):
        data = {"name": "New reward", "main_habit": self.main_habit}
        reward = Reward.objects.create(**data)
        params = {"name": "UPDATED reward"}
        response = self.client.patch(f'http://localhost:8000/habits/rewards/{reward.pk}/', data=params)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(
            response.json()['name'],
            'UPDATED reward'
        )

    def test_retrieve_reward(self):
        response = self.client.get(f'http://localhost:8000/habits/rewards/{self.reward.pk}/')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(
            response.json(),
            {'id': self.reward.pk, 'name': 'Test reward', 'description': None, 'resources': None,
             'main_habit': self.main_habit.pk}
        )

    def test_delete_support_habit(self):
        response = self.client.delete(f'http://localhost:8000/habits/rewards/{self.reward.pk}/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(Reward.objects.all().count(), 0)