from django.db import models

# Create your models here.
class FileDetails(models.Model):  
    firstname = models.CharField(max_length=20)  
    lastname = models.CharField(max_length=20)
    mobilenum= models.CharField(max_length=20)
    status=models.CharField(max_length=20)  
    email = models.EmailField() 
    fileurl=models.CharField(max_length=255)
      
