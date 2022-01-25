from django.db import models

# Create your models here.
class Employee(models.Model):
    empid = models.AutoField(primary_key=True)
    empfirstname = models.CharField(max_length=255)
    emplastname = models.CharField(max_length=255)
    gender = models.CharField(max_length=255
                              )
    DateofBirth = models.CharField(max_length=255)
    salutation = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    mobile = models.IntegerField()
    addressFirstLine = models.CharField(max_length=255)
    addressSecondLine = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    pin = models.IntegerField()
    country = models.CharField(max_length=255)   


'''
Id
FirstName
LastName
Gender
DOB
Salutation
Designation
Email
Mobile
AddressLIne1
AddressLIne2
City
State
Pin
Country
'''