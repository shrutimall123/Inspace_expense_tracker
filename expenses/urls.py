from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from expenses.views import expense_list, add_expense
from expenses.forms import UserRegistrationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LogoutView
from . import views
from django.conf import settings
from .views import login_view,CustomLogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', expense_list, name='expense_list'),
    path('add/', add_expense, name='add_expense'),
    
    path('login/', login_view, name='login'),

    path('logout/', CustomLogoutView.as_view(), name='logout'),  # Custom logout view
    path('register/', CreateView.as_view(
        template_name='register.html',
        form_class=UserRegistrationForm,
        success_url='/'
    ), name='register'),

    path('expense/create/', views.expense_create, name='expense_create'),
    path('expense/update/<int:pk>/', views.expense_update, name='expense_update'),
    path('expense/delete/<int:pk>/', views.expense_delete, name='expense_delete'),
]