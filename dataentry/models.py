from django.db import models

# Create your models here.


class Student(models.Model):
    roll_no = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Customer(models.Model):
    customer_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.customer_name


class Employee(models.Model):
    employee_id = models.CharField(max_length=10)
    employee_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    retirement = models.DecimalField(max_digits=10, decimal_places=2)
    other_benifits = models.DecimalField(max_digits=10, decimal_places=2)
    total_benifits = models.DecimalField(max_digits=10, decimal_places=2)
    total_compensation = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.employee_name} - {self.designation}'
