from django.db import models
from django.contrib.auth.models import User





# EXTENDING model
class CustomUser(User):
    avatar = models.CharField(max_length=150, default="")
    # FRIENDSHIP !!!
    friends = models.ManyToManyField('self')
    session_data_backup = models.TextField(default='')


class Post(models.Model):
    title = models.CharField(max_length=100)
    body  = models.CharField(max_length=200, default="")

    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE, default=None)

    

class Comment(models.Model):
    pass
