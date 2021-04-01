from django.db import models

# Create your models here.
class LoginInfo(models.Model):
    AccountName = models.CharField(max_length=30, primary_key=True)
    Password = models.CharField(max_length=100)
    class Meta:
        db_table = "LoginInfo"