from django.db import models

class ClassForm(models.Model):
    user = models.CharField(max_length=10000, default="")
    forms = models.CharField(max_length=10000, default="")
    returned = models.IntegerField(default=0)
    not_returned = models.IntegerField(default=0)

class period1(models.Model):
    Student = models.CharField(max_length=10000, default="")
    signedOutTime = models.CharField(max_length=10000, default="")
    signedInTime = models.CharField(max_length=10000, default="")
    Status = models.CharField(max_length=10000, default="")
    Teacher = models.CharField(max_length=1000, default="")
    EachPersonData = models.CharField(max_length=10000, default="")
    
class period2(models.Model):
    Student = models.CharField(max_length=10000, default="")
    signedOutTime = models.CharField(max_length=10000, default="")
    signedInTime = models.CharField(max_length=10000, default="")
    Status = models.CharField(max_length=10000, default="")
    Teacher = models.CharField(max_length=1000, default="")
    EachPersonData = models.CharField(max_length=10000, default="")

class period3(models.Model):
    Student = models.CharField(max_length=10000, default="")
    signedOutTime = models.CharField(max_length=10000, default="")
    signedInTime = models.CharField(max_length=10000, default="")
    Status = models.CharField(max_length=10000, default="")
    Teacher = models.CharField(max_length=1000, default="")
    EachPersonData = models.CharField(max_length=10000, default="")

class period4(models.Model):
    Student = models.CharField(max_length=10000, default="")
    signedOutTime = models.CharField(max_length=10000, default="")
    signedInTime = models.CharField(max_length=10000, default="")
    Status = models.CharField(max_length=10000, default="")
    Teacher = models.CharField(max_length=1000, default="")
    EachPersonData = models.CharField(max_length=10000, default="")
