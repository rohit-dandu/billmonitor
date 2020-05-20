from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Expense(models.Model):
    place = models.CharField(max_length=60)
    date = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

class ExpenseItem(models.Model):
    expense = models.ForeignKey(Expense, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    category = models.CharField(max_length=30)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)