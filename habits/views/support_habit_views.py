from django.db.models import Q
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import SupportHabit
from habits.paginators import HabitListPagination
from habits.permissions import IsMainHabitOwner
from habits.serializers import SupportHabitSerializer, SupportHabitCreateSerializer


class SupportHabitCreateAPIView(generics.CreateAPIView):
    """
    Creates the SupportHabit model's objects.
    """
    queryset = SupportHabit.objects.all()
    serializer_class = SupportHabitCreateSerializer
    permission_classes = [IsAuthenticated]


class SupportHabitListAPIView(generics.ListAPIView):
    """
    Returns a paginated list of the SupportHabit model's objects.
    """
    queryset = SupportHabit.objects.all()
    serializer_class = SupportHabitSerializer
    pagination_class = HabitListPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = SupportHabit.objects.filter(Q(main_habit__user=user) | Q(is_public=True))
        return queryset


class SupportHabitRetrieveAPIView(generics.RetrieveAPIView):
    """
    Returns the SupportHabit model's object.
    """
    queryset = SupportHabit.objects.all()
    serializer_class = SupportHabitSerializer
    permission_classes = [IsAuthenticated, IsMainHabitOwner]


class SupportHabitUpdateAPIView(generics.UpdateAPIView):
    """
    Updates the SupportHabit model's object.
    """
    queryset = SupportHabit.objects.all()
    serializer_class = SupportHabitSerializer
    permission_classes = [IsAuthenticated, IsMainHabitOwner]


class SupportHabitDeleteAPIView(generics.DestroyAPIView):
    """
    Delete the SupportHabit model's object.
    """
    queryset = SupportHabit.objects.all()
    serializer_class = SupportHabitSerializer
    permission_classes = [IsAuthenticated, IsMainHabitOwner]