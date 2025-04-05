from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
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


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(
        trim_whitespace=False,
        write_only=True,
        required=True
    )
    def validate(self, attrs):
        username = attrs['username']
        password = attrs['password']

        if username and password:
            user = authenticate(request=self.context['request'], username=username, password=password)

            if not user:
                raise serializers.ValidationError({"detail": "Неверный логин или пароль"})

        else:
            raise serializers.ValidationError({'detail': 'Логин и пароль обязательные поля'})

        attrs['user'] = user
        return attrs

