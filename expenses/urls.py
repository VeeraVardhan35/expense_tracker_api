from django.urls import path, include
from .views import registerView, expenseView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'expenses', expenseView, basename='expenses')

urlpatterns = [
    path('register/', registerView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenObtainPairView.as_view(), name='refresh'),
    path('', include(router.urls))
]