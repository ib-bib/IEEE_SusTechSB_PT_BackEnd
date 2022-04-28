import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    q_txt = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # Human friendly name ^

    def __str__(self):
        return self.q_txt

    def was_published(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    q = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_txt = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_txt

# Create your models here.
