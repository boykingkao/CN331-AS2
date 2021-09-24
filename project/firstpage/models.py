from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Status_choice(models.IntegerChoices):
    OPEN = 1, "open"
    CLOSE = 0, "close"


class Subject(models.Model):
    subject_code = models.CharField(max_length = 8)
    subject_name = models.CharField(max_length = 50)
    subject_semester = models.IntegerField()
    subject_year = models.IntegerField()
    subject_seat = models.IntegerField()
    count = models.IntegerField(default=0)
    status = models.IntegerField(default=Status_choice.OPEN,choices=Status_choice.choices)
    students = models.ManyToManyField(User, blank=True, related_name="students")
    
    
    
    def __str__(self) -> str:
        return f"{self.id}: {self.subject_code} {self.subject_name}"


#class student(models.Model):
    #first = models.CharField(max_length=64)
    ##subjects = models.ManyToManyField(subject, blank=True, related_name ="students" )
    #def __str__(self) -> str:
        #return f"{self.first} {self.last}"