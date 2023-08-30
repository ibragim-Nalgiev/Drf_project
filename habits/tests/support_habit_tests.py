from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit, SupportHabit
from users.models import CustomUser


class SupportHabitTestCases(APITestCase):
    def setUp(self):
        self.user_data = {'email': 'testing@mail.com', 'telegram': '@testing', "password": "12345678"}
        self.user = CustomUser.objects.create(**self.user_data)
        self.client.force_authenticate(user=self.user)
        data = {"name": "New habit", "action_time": "22:00:00",
                "action_place": "Home", "duration": "PT2M", "user": self.user}
        self.main_habit = Habit.objects.create(**data)

    def test_create_support_habit(self):
        data = {"name": "New support habit", "main_habit": self.main_habit.pk}
        response = self.client.post(reverse('habits:support_habits_create'), data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(SupportHabit.objects.all().count(), 1)
        self.assertEquals(
            response.json(),
            {'id': self.main_habit.pk, 'name': 'New support habit', 'action': None, 'action_time': None,
             'action_place': None, 'duration': None, 'is_public': False, 'main_habit': self.main_habit.pk}
        )

    def test_list_support_habit(self):
        data = {"name": "New support habit", "main_habit": self.main_habit}
        support_habit = SupportHabit.objects.create(**data)
        response = self.client.get(reverse('habits:support_habits_list'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(SupportHabit.objects.all().count(), 1)
        self.assertEquals(response.json(), {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [
                {
                    'id': support_habit.pk,
                    'main_habit': self.main_habit.pk,
                    'name': 'New support habit',
                    'action': None,
                    'action_time': None,
                    'action_place': None,
                    'duration': None,
                    'is_public': False
                }
            ]
        })

    def test_update_support_habit(self):
        data = {"name": "New support habit", "main_habit": self.main_habit}
        support_habit = SupportHabit.objects.create(**data)
        new_data = {"name": "UPDATED support habit", "main_habit": self.main_habit.pk}
        response = self.client.put(reverse('habits:support_habits_update', kwargs={"pk": support_habit.pk}),
                                   data=new_data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(
            response.json()['name'],
            'UPDATED support habit'
        )

    def test_partial_update_support_habit(self):
        data = {"name": "New support habit", "main_habit": self.main_habit}
        support_habit = SupportHabit.objects.create(**data)
        new_data = {"name": "UPDATED support habit"}
        response = self.client.patch(reverse('habits:support_habits_update', kwargs={"pk": support_habit.pk}),
                                     data=new_data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(
            response.json()['name'],
            'UPDATED support habit'
        )

    def test_retrieve_support_habit(self):
        data = {"name": "New support habit", "main_habit": self.main_habit}
        support_habit = SupportHabit.objects.create(**data)
        response = self.client.get(reverse('habits:support_habits_detail', kwargs={"pk": support_habit.pk}))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(
            response.json(),
            {'id': support_habit.pk, 'main_habit': self.main_habit.pk, 'name': 'New support habit', 'action': None,
             'action_time': None, 'action_place': None, 'duration': None, 'is_public': False}
        )

    def test_delete_support_habit(self):
        data = {"name": "New support habit", "main_habit": self.main_habit}
        support_habit = SupportHabit.objects.create(**data)
        response = self.client.delete(reverse('habits:support_habits_delete', kwargs={"pk": support_habit.pk}))
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(SupportHabit.objects.all().count(), 0)
