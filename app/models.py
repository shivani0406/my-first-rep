from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    email      = models.EmailField(max_length=50 , unique=True)
    mob_no     = models.IntegerField()
    is_deleted = models.BooleanField(default = False)
    salary     = models.IntegerField(default=25000)

    def __str__(self):
        return str(self.first_name)
    
'''one to one relationship'''
   
    
class  Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email       = models.EmailField(unique = True)

    def __str__(self):
        return str(self.first_name)

class Profile(models.Model):
    person = models.OneToOneField(Person , on_delete=models.CASCADE)            #relation batan padega person se agar person delete 
    bio = models.TextField()                                                     #hua to usee related profile bhi delete ho jayegi
    address =models.CharField(max_length=100)                                   # profile delete hui to person delete ni hoga 
                                                                              #coz profile se person ka relation diya hai
    
    def __str__(self):
        return str(self.bio)


'''many to many relationship'''

class Fueltype(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)
    

    class Meta:                                       #to change table name
        db_table = "fuel"


class Cartype(models.Model):
    name = models.CharField(max_length=50)
    fueltype = models.ManyToManyField(Fueltype)

    def __str__(self):
        return str(self.name)
    
    class Meta:
        db_table = "car"

    
