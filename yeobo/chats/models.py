from django.db import models

class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    chat = models.CharField(max_length=400)
