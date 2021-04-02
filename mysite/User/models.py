from django.db import models

# Create your models here.
class Enrollment(models.Model):
    NetId = models.CharField(max_length=10, primary_key = True)
    CRN = models.CharField(max_length=50)
    class Meta:
        db_table = "Enrollment"
        unique_together = (("NetId", "CRN"),)

    def __str__(self):
        return self.NetId
