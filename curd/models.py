from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_id = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length=50, null=True, blank =True)
    last_name = models.CharField(max_length=50, null=True, blank =True)
    salary = models.IntegerField()
    picture = models.ImageField(upload_to='pics')
    mob_no = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    
    class Meta:
        db_table = "Employee"

class Projects(models.Model):
    emp_id= models.ForeignKey(to=Employee, on_delete=models.CASCADE)
    project_id= models.CharField(max_length=5)
    project_name= models.CharField(max_length=255)
    project_duration = models.DateField()
    project_status=models.BooleanField(default=False)