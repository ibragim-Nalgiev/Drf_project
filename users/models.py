from django.contrib.auth.models import AbstractUser
from django.db import models

from users.manager import UserManager
from users.services import upload_path

NULLABLE = {'null': True, 'blank': True}


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='user_email', max_length=100, unique=True)
    phone = models.CharField(verbose_name='user_phone', max_length=50, **NULLABLE)
    telegram = models.CharField(verbose_name='telegram', max_length=50, unique=True)
    chat_id = models.CharField(verbose_name='telegram_chat_id', max_length=50, unique=True, **NULLABLE)
    avatar = models.ImageField(verbose_name='user_avatar', upload_to=upload_path, **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()