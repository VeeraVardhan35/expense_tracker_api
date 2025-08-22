from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsOwner
from .serializers import registerSerializer, expenseSerializer
from .models import Expense
from datetime import date, timedelta, datetime

class registerView(generics.CreateAPIView):
    serializer_class = registerSerializer
    permission_classes = [AllowAny]

class expenseView(viewsets.ModelViewSet):
    serializer_class = expenseSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        qs = Expense.objects.filter(user=self.request.user)
        params = self.request.query_params

        # Category filter
        category = params.get('category')
        if category:
            qs = qs.filter(category=category)

        # Date range filter
        range_param = params.get('range')
        start_param = params.get('start')
        end_param = params.get('end')

        today = date.today()
        if range_param:
            if range_param == 'week':
                qs = qs.filter(date__gte=today - timedelta(days=7))
            elif range_param == 'month':
                qs = qs.filter(date__gte=today - timedelta(days=30))
            elif range_param == '3months':
                qs = qs.filter(date__gte=today - timedelta(days=90))
        else:
            try:
                if start_param and end_param:
                    start = datetime.strptime(start_param, '%Y-%m-%d').date()
                    end = datetime.strptime(end_param, '%Y-%m-%d').date()
                    qs = qs.filter(date__gte=start, date__lte=end)
                elif start_param:
                    start = datetime.strptime(start_param, '%Y-%m-%d').date()
                    qs = qs.filter(date__gte=start)
                elif end_param:
                    end = datetime.strptime(end_param, '%Y-%m-%d').date()
                    qs = qs.filter(date__lte=end)
            except ValueError:
                pass

        return qs.order_by('-date', '-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
