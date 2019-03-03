from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    Question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('published date')

    def __str__(self):
        return self.Question_text
    def was_pub_recently(self):
        return self.pub_date>=timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    Choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.Choice_text


