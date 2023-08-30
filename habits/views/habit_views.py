from django.db.models import Q
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginators import HabitListPagination
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer, HabitCreateSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """
    Creates the Habit model's objects.
    """
    serializer_class = HabitCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitListAPIView(generics.ListAPIView):
    """
    Returns a paginated list of the Habit model's objects.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitListPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Habit.objects.filter(Q(user=user) | Q(is_public=True))
        return queryset


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """
    Returns the Habit model's object.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """
    - Works both for PUT and PATCH methods. Updates the Habit model's object.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDeleteAPIView(generics.DestroyAPIView):
    """
    Deletes the Habit model's object.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]