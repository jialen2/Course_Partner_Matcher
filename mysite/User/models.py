from django.db import models

# Create your models here.
class Enrollment(models.Model):
    #id = models.CharField(max_length=10, primary_key = True)
    NetId = models.CharField(max_length=10)
    CRN = models.CharField(max_length=50)
    class Meta:
        db_table = "Enrollment"
        unique_together = (("NetId", "CRN"),)

#    def __str__(self):
#        return self.NetId

class Courses(models.Model):
    CRN = models.CharField(max_length = 10, primary_key = True)
    CourseTitle = models.CharField(max_length = 100)
    CourseNumber = models.CharField(max_length = 50)
    Department = models.CharField(max_length = 100)
    Section = models.CharField(max_length = 50)
    ScheduleType = models.CharField(max_length = 50)
    Instructor = models.CharField(max_length = 50)
    MeetingTime = models.CharField(max_length = 50)
    class Meta:
        db_table = "Courses"

class LoginInfo(models.Model):
    AccountName = models.CharField(max_length=30, primary_key=True)
    Password = models.CharField(max_length=100)
    class Meta:
        db_table = "LoginInfo"

    def __str__(self):
        return self.AccountName

class Students(models.Model):
    NetId = models.CharField(max_length = 10, primary_key = True)
    FirstName = models.CharField(max_length = 50)
    LastName = models.CharField(max_length = 50)
    Preferred_Work_Time = models.CharField(max_length = 50)
    SchoolYear = models.CharField(max_length = 50)
    ContactInfo = models.CharField(max_length = 255)
    OtherInfo = models.CharField(max_length = 255)
    class Meta:
        db_table = "Students"

