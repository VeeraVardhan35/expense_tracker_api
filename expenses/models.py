# expenses/models.py
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()   # get Django's User model (default)

CATEGORY_CHOICES = [
    ('groceries', 'Groceries'),
    ('leisure', 'Leisure'),
    ('electronics', 'Electronics'),
    ('utilities', 'Utilities'),
    ('clothing', 'Clothing'),
    ('health', 'Health'),
    ('others', 'Others'),
]

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    amount = models.DecimalField(max_digits=10, decimal_places=2)   # money: use DecimalField
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='others')
    description = models.TextField(blank=True)
    date = models.DateField(default=timezone.now)   # which day the expense happened
    created_at = models.DateTimeField(auto_now_add=True)  # auto timestamp

    class Meta:
        ordering = ['-date', '-created_at']  # newest first

    def __str__(self):
        return f'{self.user.username} - {self.category} - {self.amount}'
