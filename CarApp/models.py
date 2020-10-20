from django.db import models

# Create your models here.
class CarModel(models.Model):

    age = models.CharField(max_length=3)
    salary=models.CharField(max_length=12)

    
    
    def __str__(self):
        return self.age


    

   


