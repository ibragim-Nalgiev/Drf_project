from django.urls import path
from rest_framework.routers import DefaultRouter

from habits.apps import HabitsConfig
from habits.views import HabitListAPIView, HabitCreateAPIView, HabitUpdateAPIView, HabitDeleteAPIView, \
    HabitRetrieveAPIView
from habits.views.reward_views import RewardViewSet
from habits.views.support_habit_views import SupportHabitListAPIView, SupportHabitRetrieveAPIView, \
    SupportHabitCreateAPIView, SupportHabitUpdateAPIView, SupportHabitDeleteAPIView

app_name = HabitsConfig.name

router = DefaultRouter()
router.register(r'habits/rewards', RewardViewSet, basename='rewards')

urlpatterns = [
    # main habits
    path('habits/', HabitListAPIView.as_view(), name='habits_list'),
    path('habits/detail/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habits_detail'),
    path('habits/create/', HabitCreateAPIView.as_view(), name='habits_create'),
    path('habits/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habits_update'),
    path('habits/delete/<int:pk>/', HabitDeleteAPIView.as_view(), name='habits_delete'),

    # support habits
    path('habits/support-habits/', SupportHabitListAPIView.as_view(), name='support_habits_list'),
    path('habits/support-habits/detail/<int:pk>/', SupportHabitRetrieveAPIView.as_view(),
         name='support_habits_detail'),
    path('habits/support-habits/create/', SupportHabitCreateAPIView.as_view(),
                       name='support_habits_create'),
    path('habits/support-habits/update/<int:pk>/', SupportHabitUpdateAPIView.as_view(),
         name='support_habits_update'),
    path('habits/support-habits/delete/<int:pk>/', SupportHabitDeleteAPIView.as_view(),
         name='support_habits_delete'),

    # rewards - via ViewSet endpoints
] + router.urls
