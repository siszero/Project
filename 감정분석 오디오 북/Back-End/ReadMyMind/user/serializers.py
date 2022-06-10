from rest_framework import serializers
from .models import User, Book, Music, RecommendedBook

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'name', 'date']

# class RecommendedBookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RecommendedBook
#         fields = ['id', 'title', 'writer', 'content', 'book_id']

class BookSerializer(serializers.ModelSerializer):
    # recommend = RecommendedBookSerializer(many=True)
    class Meta:
        model = Book
        fields = ['id', 'category', 'title', 'writer', 'content', 'image']
        # fields = ['id', 'category', 'title', 'writer', 'content', 'recommend']

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['id', 'category', 'title']

class RecommendedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendedBook
        fields = ['id', 'title', 'writer', 'content', 'image', 'book_id']