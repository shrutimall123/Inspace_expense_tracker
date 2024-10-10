from django.contrib import admin

# Register your models here.
from .models import Expense

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('user', 'description', 'amount', 'date')  # Fields to display in the admin list
    search_fields = ('description',)  # Add a search box for the description field
    list_filter = ('date',)  # Add a filter option for the date field

admin.site.register(Expense, ExpenseAdmin)