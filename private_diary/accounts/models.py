from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
#AbstractUserクラスを継承したCustomUserクラス
class CustomUser(AbstractUser):
    """ 拡張ユーザーモデル """

    class Mata:
        verbose_name_plural = 'CustomUser'