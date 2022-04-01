from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
class Feedback(models.Model):
  ''' Отзыв о чем угодно. '''
  text = models.CharField(verbose_name='Отзыв', max_length=5000, blank=True)
  grade = models.IntegerField(verbose_name='Оценка', default=1)
  # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  subject = models.CharField(verbose_name='Объект', max_length=100)

