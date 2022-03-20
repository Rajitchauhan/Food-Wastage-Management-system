from django.db import models
from django.contrib.auth.models import User


class Donate_Food(models.Model):
    user  = models.OneToOneField(User , on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    Address = models.CharField(max_length=100)
    Donate_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100 , default="panding...")
    message = models.CharField(max_length=100 , default='Thank you for your support  , our agent will contact you')
    FeedBack = models.TextField(default='.')
    #author = models.ForeignKey(User , default=None , on_delete='')


    def __str__(self):
        return self.user.username
