from django.db import models

# Create your models here.

class Student(models.Model):
    name= models.CharField(max_length= 100)
    roll_number= models.IntegerField(default=0)
    GENDER_CHOICES=(
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender= models.CharField(max_length=1, choices=GENDER_CHOICES)
    fav_subject= models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.name} - {self.roll_number}"