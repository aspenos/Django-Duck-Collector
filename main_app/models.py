from django.db import models
from datetime import date
from django.contrib.auth.models import User


MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)
# Create your models here.

class Pond(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Duck(models.Model):
    name = models.CharField(max_length=100, default='Unknown')
    breed = models.CharField(max_length=100, default='Unknown')
    description = models.TextField(max_length=250, default='Unknown')
    age = models.IntegerField(default=0)
    ponds = models.ManyToManyField('Pond', related_name='ducks')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
  
    def __str__(self):
      return self.name
  
  # Add an indented block of code here
  
  
class Feeding(models.Model):
  date = models.DateField('Feeding Date')
  meal = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=MEALS,
    # set the default value for meal to be 'B'
    default=MEALS[0][0]
  )

  duck = models.ForeignKey(Duck, on_delete=models.CASCADE)

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_meal_display()} on {self.date}"

  class Meta:
    ordering = ['-date']

