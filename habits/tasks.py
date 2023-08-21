from telebot import TeleBot
from config import settings
from config.celery import app
from habits.models import Habit


@app.task
def send_telegram_message(habits_id):
    """Отправка сообщения через бот TG"""
    habit = Habit.objects.get(id=habits_id)
    bot = TeleBot(settings.TG_BOT_TOKEN)
    message = f"Напоминание о выполнении привычки {habit.action} в {habit.time} в {habit.place}"
    bot.send_message(habit.owner.chat_id, message)
