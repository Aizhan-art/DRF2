from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book, Category


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')


class BookListSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    category = CategorySerializer()

    class Meta:
        model = Book
        fields = ('id', 'title', 'description', 'created_date', 'author', 'category')


class BookCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Book
        fields = ('title', 'description', 'author', 'category')

    def validate(self, data):
        if 'матраимов' in data['title'].lower():
            raise serializers.ValidationError({'title':'Cлово Матраимов запрещенно!'})

        return data


class BookUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'description', 'category')
