from django.db import models
import datetime
from django.core.exceptions import ValidationError

def validate_date(value):
    if value>datetime.date.today():
        raise ValidationError("Don't select future date")
    else:
        return value
    
    
class Equipment(models.Model):
    name=models.CharField(max_length=100)
    created_date=models.DateField(default=datetime.datetime.now,
        validators=[validate_date])
    
    def __str__(self):
        return self.name
    
class Executive(models.Model):
    emp_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    joining_date=models.DateField()
    equipment_name=models.ManyToManyField(Equipment)
    
    def __str__(self):
        return str(self.emp_id)
