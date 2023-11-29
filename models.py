from django.db import models

from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class Home(models.Model):
    teacher=models.CharField(max_length=122)
    score=models.IntegerField(default=0,
                              validators=[
                                  MaxValueValidator(5),
                                  MinValueValidator(0),
                              ])
    feedback=models.TextField(default='Your Default Value')
    date=models.DateTimeField()

    class Meta:
        ordering = ['teacher','score']
    
    
class Attendance(models.Model):
    teacher=models.CharField(max_length=50,default='Your Default Value')
    branch=models.CharField( max_length=50,default='Your Default Value')
    year=models.CharField(max_length=122,default='Your Default Value') 
    section=models.CharField(max_length=122,default='Your Default Value') 
    email=models.CharField(max_length=122,default='Your Default Value') 
    date=models.DateField()   

    class Meta:
        ordering = ['id','date','branch','year','section','email']

class Branch(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Year(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Section(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Email(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['section','name']
