from rest_framework import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.response import Response
from rest_framework import viewsets, generics
from django.contrib.auth.models import User
from .models import Cat, Category
from .serializers import CatSerializer, CategorySerializer, UserSerializer
from rest_framework.permissions import BasePermission



class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()  # ← ОБЯЗАТЕЛЬНО!
    serializer_class = CatSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Cat.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()  # ← ОБЯЗАТЕЛЬНО!
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]