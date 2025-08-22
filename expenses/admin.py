from django.contrib import admin
from .models import Expense
# Register your models here.

@admin.register(Expense)
class expenseAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'amount', 'category', 'date', 'created_at']
    list_filter = ['category', 'date']
    search_fields = ['user__username', 'description']