from django.db import models
from django.contrib.auth.models import User

class Departments(models.Model):
    Department_id = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=150)

    class Meta:
        managed = False  
        db_table = 'departments'  

    def __str__(self):
        return self.DepartmentName 
    
class Services(models.Model):
    ServiceId = models.AutoField(primary_key=True)
    Department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    #DepartmentId =  models.CharField(max_length=255)
    #DepartmentName = models.CharField(max_length=255)
    NameOfService = models.CharField(max_length=255)
    Cost = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'services'

class Appointment(models.Model):
    AppointmentID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=150)
    Phone = models.CharField(max_length=13)
    Department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    #DepartmentName = models.CharField(max_length=255)
    #DepartmentName = models.ForeignKey(Departments, on_delete=models.CASCADE)
    NameOfService = models.CharField(max_length=150)
    AppointmentDate = models.DateField()
    AppointmentTime = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
     
    class Meta:
        db_table = 'appointments'

    def __str__(self):
        return f"{self.Name} - {self.Department.DepartmentName}"

    

    
