from django.db import models

# Create your models here.
class tasks(models.Model):
    p_id=models.IntegerField()
    test=models.CharField(max_length=200)
    isdone=models.BooleanField(default=False)
