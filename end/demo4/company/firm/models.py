from django.db import models

# Create your models here.

class Branch(models.Model):
    name=models.CharField(max_length=15,verbose_name="部门名")

    def __str__(self):
        return self.category


class Staff(models.Model):
    name=models.CharField(max_length=10,verbose_name="姓名")
    money=models.CharField(max_length=20,verbose_name="工资")
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE,related_name='staff')

    def __str__(self):
        return self.name
