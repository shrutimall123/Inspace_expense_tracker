from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Expense
from .forms import ExpenseForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.views import LoginView 



@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    total_expenses = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    
    category = request.GET.get('category')
    date = request.GET.get('date')
    
    if category:
        expenses = expenses.filter(category=category)
    if date:
        expenses = expenses.filter(date=date)
    
    context = {
        'expenses': expenses,
        'total_expenses': total_expenses,
    }
    return render(request, 'expense_list.html', context)

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'form': form})



def custom_logout(request):
    logout(request)  
    return render(request, 'loggedout.html')



@login_required  
def expense_create(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)  
            expense.user = request.user 
            expense.save() 
            return redirect('expense_list')  
    else:
        form = ExpenseForm()
    return render(request, 'expense_create.html', {'form': form})

# Update an existing expense
def expense_update(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expense_form.html', {'form': form})

# Delete an expense
def expense_delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    return render(request, 'expense_confirm_delete.html', {'expense': expense})

class CustomLoginView(LoginView):
    template_name = 'login.html' 


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')  # Redirect to login after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('expense_list')
    return render(request, 'login.html')

from django.contrib.auth.views import LogoutView

class CustomLogoutView(LogoutView):
    template_name = 'loggedout.html'  # Redirect to a dedicated logout page

    def get_next_page(self):
        return super().get_next_page() or '/'

def logout_view(request):
    logout(request)
    return redirect('loggedout') 

class CustomLogoutView(LogoutView):
    template_name = 'loggedout.html'


