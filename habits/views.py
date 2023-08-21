from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.pagination import HabitPagination
from habits.serializers import HabitSerializers
from habits.services import create_habit_schedule
from users.models import UserRoles


class HabitsViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializers
    queryset = Habit.objects.all()
    # permission_classes = [IsAuthenticated]
    pagination_class = HabitPagination

    def perform_create(self, serializer) -> None:
        """Сохраняет новому объекту владельца и создает задачу"""
        serializer.save(owner=self.request.user)
        habit = serializer.save()
        create_habit_schedule(habit)

    def get_queryset(self):
        """Список привычек только для юзера или модератора"""
        user = self.request.user
        if user.is_staff or user.is_superuser or user.role == UserRoles.MODERATOR:
            return Habit.objects.all()
        else:
            return Habit.objects.filter(owner=user)


class HabitsListView(generics.ListAPIView):
    serializer_class = HabitSerializers
    queryset = Habit.objects.all()
    # permission_classes = [IsAuthenticated]
    pagination_class = HabitPagination

    def get_queryset(self):
        """Список публичных привычек"""
        user = self.request.user
        if user.is_staff or user.is_superuser or user.role == UserRoles.MODERATOR:
            return Habit.objects.all()
        else:
            return Habit.objects.filter(public=True)
