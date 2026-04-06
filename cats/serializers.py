from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Cat, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ('id', 'name', 'color', 'birth_year', 'image', 'category')

    def validate_birth_year(self, value):
        if value and value > 2026:
            raise serializers.ValidationError("Год рождения не может быть в будущем!")
        return value

    def validate_name(self, value):
        if not value or value.isspace():
            raise serializers.ValidationError("Имя не может быть пустым!")
        return value.strip()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # ← ЯВНО объявляем поле!

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        # Извлекаем пароль
        password = validated_data.pop('password')

        # Создаем пользователя
        user = User.objects.create_user(**validated_data)
        user.set_password(password)  # ← Правильно хэшируем
        user.save()
        return user