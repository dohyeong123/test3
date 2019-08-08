from django.db import models

# Create your models here.
class Member(models.Model):
    member_name = models.CharField(max_length = 20)
    member_code = models.CharField(max_length = 20)
    attend=models.BooleanField(default=True)