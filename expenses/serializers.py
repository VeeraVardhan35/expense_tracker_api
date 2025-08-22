from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Expense

User = get_user_model()

class registerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'], email=validated_data['email'], password=validated_data['password'])
        return user


class expenseSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')    
    
    class Meta:
        model = Expense
        fields = ['id', 'user', 'amount', 'category', 'description', 'date', 'created_at']
