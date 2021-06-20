from django.db import models
from django.contrib.auth.models import UserManager

# Create your models here.
        
# Create your models here.
class State(models.Model):
    state_and_UTs = models.CharField(max_length=200)
    state_id = models.IntegerField()
    def __str__(self):
        return str(self.state_id)

class Student(models.Model):
    name = models.CharField(max_length=200)
    roll_number = models.IntegerField()
   
    state_id = models.ForeignKey(State, on_delete=models.DO_NOTHING)
    def __str__(self):
        return str(self.roll_number)


class Marks(models.Model):
    roll_number = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    marks = models.IntegerField()

    def __str__(self):
        return str(self.roll_number)



