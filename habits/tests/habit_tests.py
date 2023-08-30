from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import CustomUser


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user_data = {'email': 'testing@mail.com', 'telegram': '@testing', "password": "123"}
        self.user = CustomUser.objects.create(**self.user_data)
        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        data = {"name": "New habit", "action_time": "22:00:00",
                "action_place": "Home", "duration": "PT2M", "user": self.user.pk}
        response = self.client.post(reverse('habits:habits_create'), data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(
            response.json()['name'], "New habit")

        self.assertEquals(Habit.objects.all().count(), 1)

    def test_list_habit(self):
        data = {"name": "New habit", "action_time": "22:00:00",
                "action_place": "Home", "duration": "PT2M"}
        self.client.post(reverse('habits:habits_create'), data=data)
        response = self.client.get(reverse('habits:habits_list'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(Habit.objects.all().count(), 1)
        self.assertEquals(
            response.json()['results'][0]['name'],
            'New habit'
        )

    def test_update_habit(self):
        data = {"name": "New habit", "action_time": "22:00:00",
                "action_place": "Home", "duration": "PT2M", "user": self.user}
        habit = Habit.objects.create(**data)
        new_data = {"name": "UPDATED habit", "action_time": "22:00:00",
                    "action_place": "Home", "duration": "PT2M"}
        response = self.client.put(reverse('habits:habits_update', kwargs={"pk": habit.pk}), data=new_data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(
            response.json()['name'],
            'UPDATED habit'
        )

    def test_partial_update_habit(self):
        data = {"name": "New habit", "action_time": "22:00:00",
                "action_place": "Home", "duration": "PT2M", "user": self.user}
        habit = Habit.objects.create(**data)
        new_data = {"name": "UPDATED habit"}
        response = self.client.patch(reverse('habits:habits_update', kwargs={"pk": habit.pk}), data=new_data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(
            response.json()['name'],
            'UPDATED habit'
        )

    def test_retrieve_habit(self):
        data = {"name": "New habit", "action_time": "22:00:00",
                "action_place": "Home", "duration": "PT2M", "user": self.user}
        habit = Habit.objects.create(**data)
        response = self.client.get(reverse('habits:habits_detail', kwargs={"pk": habit.pk}))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(
            response.json(),
            {'id': habit.pk, 'name': 'New habit', 'user': self.user.pk, 'action': None, 'action_time': '22:00:00',
             'action_place': 'Home',
             'duration': '00:02:00', 'regularity': 'daily', 'is_public': False, 'has_support_habits': False,
             'support_habit': [], 'has_reward': False, 'habit_reward': []}
        )

    def test_delete_habit(self):
        data = {"name": "New habit", "action_time": "22:00:00",
                "action_place": "Home", "duration": "PT2M", "user": self.user}
        habit = Habit.objects.create(**data)
        response = self.client.delete(reverse('habits:habits_delete', kwargs={"pk": habit.pk}))
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(Habit.objects.all().count(), 0)