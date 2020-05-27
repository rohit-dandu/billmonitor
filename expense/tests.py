from django.test import TestCase
from .models import Expense
import datetime
from decimal import Decimal

# Create your tests here.
# Testing the expense model
class ExpenseTest(TestCase):
    def create_expense(self, id=27, place='test', date='2020-01-31', total=9.99):
        return Expense.objects.create(place=place, 
        date = datetime.datetime.strptime(date, "%Y-%m-%d").date(), 
        total=Decimal(total))
    
    def test_create_expense(self):
        ex = self.create_expense()
        self.assertTrue(isinstance(ex, Expense))