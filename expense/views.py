from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import datetime
from decimal import Decimal
from .models import Expense, ExpenseItem
from django.views.generic import View, ListView
from django.views.generic.detail import DetailView
from .totalContext import TotalContext
from .dispatcher import Dispatcher
from .totalInterceptor import TotalInterceptor
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required(login_url='/login')
def expense(request):
    # return HttpResponse("<h1>BillMonitor!</h1>")
    expenses = [obj.id for obj in Expense.objects.filter(user=request.user)]
    gro_total = 0
    sna_total = 0
    ute_total = 0
    oth_total = 0
    for expense in expenses:
        gro_total += cal_total(ExpenseItem.objects.filter(expense_id=expense).filter(category='gro'))
        sna_total += cal_total(ExpenseItem.objects.filter(expense_id=expense).filter(category='sna'))
        ute_total += cal_total(ExpenseItem.objects.filter(expense_id=expense).filter(category='ute'))
        oth_total += cal_total(ExpenseItem.objects.filter(expense_id=expense).filter(category='oth'))
    print(gro_total, sna_total, ute_total, oth_total)
    return render(request, 'expense/expense.html', {'g': gro_total, 's': sna_total, 'u': ute_total, 'o': oth_total})

def cal_total(items):
    total = 0
    for o in items:
        total += o.quantity * o.price
        # total += o['quantity'] * o['price']
    return total

# Product
class Bill: 
    def __init__(self):
        self._place = None
        self._date = None
        self._total = None
    
    def setPlace(self, place):
        self._place = place
    
    def setDate(self, date):
        self._date = date
    
    def setTotal(self, total):
        self._total = total
    
    def getPlace(self):
        return self._place
    
    def getDate(self):
        return self._date
    
    def getTotal(self):
        return self._total

# builder
class Builder:

    def buildPlace(self): pass
    def buildDate(self): pass
    def cleanList(self): pass
    def buildTotal(self): pass
    def buildModel(self): pass

# concrete builder
class BillBuilder(View, Builder):

    def __init__(self, values, user):
        self.values = values
        self.user = user
        self._place = None
        self._date = None
        self._total = None
        self._token = None
        self._submit = None
    
    bill = Bill()
    
    def buildPlace(self):
        self._place = self.values.pop(0)
        self.bill.setPlace(self._place)
    
    def buildDate(self):
        self._date = datetime.datetime.strptime(self.values.pop(0), "%Y-%m-%d").date()
        self.bill.setDate(self._date)
    
    def cleanList(self):
        self._token = self.values.pop()
        self._submit = self.values.pop()
    
    def buildTotal(self):
        self._total = Decimal(self.values.pop())
        self.bill.setTotal(self._total)
    
    def buildModel(self):
        print(self._place, self._date)
        eb = Expense(place=self._place, date=self._date, total=self._total, user=self.user)
        eb.save()
        for i in range(0, len(self.values)-1):
            if len(self.values) > 0:
                name, cat, qty, price = self.values[0:4]
                ei = ExpenseItem(name=name, category=cat, quantity=int(qty), price=Decimal(price), expense=eb)
                ei.save()
                print(name, cat, qty, price)
                del self.values[0:4]

# bill director
class BillDirector:
    _builder = None
    def setBuilder(self, builder):
        self._builder = builder
    # Assemble the bill
    def construct(self):
        self._builder.buildPlace()
        self._builder.buildDate()
        self._builder.cleanList()
        self._builder.buildTotal()
        self._builder.buildModel()

class BillView(View):

    def onrequest(self):
        context = TotalContext(self.request.user, self.request.POST['total'])
        dispatcher = Dispatcher()
        dispatcher.register(TotalInterceptor)
        dispatcher.dispatch(context)

    def post(self, request, *args, **kwargs):
        values = list(request.POST.dict().values())
        billbuilder = BillBuilder(values, user=request.user)
        director = BillDirector()
        director.setBuilder(billbuilder)
        director.construct()
        self.onrequest()
        return HttpResponseRedirect('/')