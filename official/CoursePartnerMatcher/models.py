from django.db import models

# Create your models here.
class Enrollment(models.Model):
    NetId = models.CharField(max_length=10)
    CRN = models.CharField(max_length=50)
    class Meta:
        db_table = "Enrollment"
        unique_together = (("NetId", "CRN"),)

    def __str__(self):
        return self.NetId

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

    def __str__(self):
        return self.CRN

class LoginInfo(models.Model):
    AccountName = models.CharField(max_length = 30, primary_key = True)
    Password = models.CharField(max_length = 100)
    class Meta:
        db_table = "LoginInfo"

    def __str__(self):
        return self.AccountName

class Students(models.Model):
    time = [('early morning', 'early morning'), ('morning', 'morning'), ('noon', 'noon'), ('afternoon', 'afternoon'), ('evening', 'evening'), ('late night', 'late night')]
    schoolyear = [('freshman', 'freshman'), ('sophomore', 'sophomore'), ('junior', 'junior'), ('senior', 'senior'), ('masters', 'masters'), ('PhD', 'PhD')]
    NetId = models.CharField(max_length = 10, primary_key = True)
    FirstName = models.CharField(max_length = 50, blank=True)
    LastName = models.CharField(max_length = 50, blank=True)
    Preferred_Work_Time = models.CharField(max_length = 50, choices = time)
    SchoolYear = models.CharField(max_length = 50, choices=schoolyear)
    ContactInfo = models.CharField(max_length = 255, blank=True)
    OtherInfo = models.CharField(max_length = 255, blank=True)
    class Meta:
        db_table = "Students"

class Instructors(models.Model):
    Name = models.CharField(max_length = 50)
    Department = models.CharField(max_length = 100)
    class Meta:
        db_table = "Instructors"
        unique_together = (("Name", "Department"),)

class Departments(models.Model):
    DeptName = models.CharField(max_length = 100, primary_key = True)
    DeptHead = models.CharField(max_length = 50)
    DeptOffice = models.CharField(max_length = 300)
    DeptPhone = models.CharField(max_length = 50)
    class Meta:
        db_table = "Departments"

class Home(models.Model):
    NetId = models.CharField(max_length=10, primary_key = True)
    Department =  models.CharField(max_length=500, blank=True)
    class Meta:
        db_table = "Home"
        unique_together = (("NetId", "Department"),)