from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView, DeleteView
from .models import Expense, ExpenseItem
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HistoryList(LoginRequiredMixin, ListView):
    
    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(HistoryList, self).get_context_data(**kwargs)
        return context

class HistoryView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        return ExpenseItem.objects.filter(expense_id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(HistoryView, self).get_context_data(**kwargs)
        print(context)
        return context