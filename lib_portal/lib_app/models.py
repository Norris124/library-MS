from django.db import models

# Create your models here.
class Student(models.Model) :

    def __str__(self):
        return self.Student_name
    
    Student_name = models.CharField(max_length= 200)
    register_id = models.CharField(max_length=200)
    Student_contact = models.CharField(max_length = 200)
    active = models.BooleanField(default=True)

