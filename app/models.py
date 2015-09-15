from django.db import models
from django.utils import timezone

# Create your models here.
class ExpensesRegistry(models.Model):
	
	expenses =  models.CharField(max_length = 50)
	income = models.CharField(max_length = 50)
	income_date = models.DateTimeField()
	expenses_date = models.DateTimeField()
	expenses_concept = models.TextField(max_length = 50)
	income_concept = models.TextField(max_length = 50)
