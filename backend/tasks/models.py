from django.db import models
from users.models import CustomUser

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ForeignKey(CustomUser, on_delete=models) # this did not work so I used AI to show me this down there WRITE IN CHALLENGE REPORT
    # assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
# Create your models here.
