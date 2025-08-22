import random
from datetime import date, timedelta
from expenses.models import Expense, CATEGORY_CHOICES
from django.contrib.auth import get_user_model

User = get_user_model()

def run():
    user = User.objects.get(username="veera")
    categories = [c[0] for c in CATEGORY_CHOICES]

    for _ in range(1000):
        Expense.objects.create(
            user=user,
            amount=round(random.uniform(10, 500), 2),
            category=random.choice(categories),
            description="Auto-generated expense",
            date=date.today() - timedelta(days=random.randint(0, 365))
        )

    print(f"✅ 1000 expenses inserted for user: {user.username}")

# 👇 This makes it run automatically
run()
