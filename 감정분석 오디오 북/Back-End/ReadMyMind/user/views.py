from django.db.models import Max
from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Book, Music, RecommendedBook
from .serializers import UserSerializer, BookSerializer, MusicSerializer, RecommendedBookSerializer
from django.http import HttpResponse
from django.core import serializers

import random


@api_view(['GET'])
def user_getAll(request):
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

# 책 랜덤으로

# @api_view(['GET'])
# def book_selectOne(request, emotion):
#     if request.method == 'GET':
#         # AI 모델 통해 어떤 감정인지 전달받기
#         randomBookList = Book.objects.filter(category=emotion)
#         serializer = BookSerializer(random.choice(randomBookList))  # 책 필터에 걸린 불러와서
#         return Response(serializer.data)


# 한 권만
@api_view(['GET'])
def book_selectOne(request, id):
    if request.method == 'GET':
        # java.lang.IllegalStateException: Expected BEGIN_OBJECT but was BEGIN_ARRAY at line 1 column 2 path $
        # 위 오류 떠서 objects에서 array로 수정
        randomBookList = Book.objects.filter(id = id)
        serializer = BookSerializer(randomBookList, many=True)  # 책 필터에 걸린 불러와서
        return Response(serializer.data)


@api_view(['GET'])
def music_selectOne(request, emotion):
    if request.method == 'GET':
        # AI 모델 통해 어떤 감정인지 전달받기
        randomMusicList = Music.objects.filter(category=emotion)
        serializer = MusicSerializer(random.choice(randomMusicList))  # 책 필터에 걸린 불러와서

        return Response(serializer.data)



@api_view(['GET'])
def book_recommend(request, book_pk):
    if request.method == 'GET':
        # AI 모델 통해 어떤 감정인지 전달받기
        recommendedBookList = RecommendedBook.objects.filter(book_id=book_pk)
        serializer = RecommendedBookSerializer(recommendedBookList, many=True)  # 책 필터에 걸린 불러와서

        return Response(serializer.data)

        #recommendedBookList = RecommendedBook.objects.filter(book_id=book_pk)
        #serializer = serializers.serialize('json', recommendedBookList)
        #return HttpResponse(serializer, content_type="text/json-comment-filtered")

# @api_view(['GET'])
# def book_recommend(request):
#     if request.method == 'GET':
#         # AI 모델 통해 어떤 감정인지 전달받기
#         recommendedbook = RecommendedBook.objects.all()
#         recommendedbook_filterList = MusicSerializer(recommendedbook, many=True)  # 책 필터에 걸린 불러와서
#
#         print(recommendedbook_filterList)
#
#         # 랜덤으로 한개 추출
#         # serializer = random.choice(music_filterList)
#         return Response(recommendedbook_filterList.data)

# @api_view(['GET'])
# def book_random(request, emotion): # emotion: AI통해서 나온 감정
#     if request.method == 'GET':
#         # AI 모델 통해 어떤 감정인지 전달받기
#         randomBookList = Book.objects.filter(category=emotion)
#
#         serializer = BookSerializer(random.choice(randomBookList))  # 책 필터에 걸린 불러와서
#         return Response(serializer.data)

# AI 모델 통해 어떤 감정인지 전달받기
        # 받은 감정이 happy라면
        # feeling = 'happy'

        # 총 데이터 수
        # max_id = Book.objects.all().aggregate(max_id=Max("id" == feeling))['max_id']
        # print(max_id)
        # pk = random.randint(1, 25)
        # print(pk)

        # book_filterList = Book.objects.get(id=pk)   # id랑 랜덤으로 뽑은 애랑 같은걸 뽑아오고 싶다고!!!!!!

        # for i in Book:
        #     if Book.id == pk:
        #         print(i.objects.all())
        # book_filterList = BookSerializer(id=pk)    # 책 필터에 걸린 불러 와서
        # print(book_filterList)

        # 되는 걸
        # book = Book.objects.all()
        # book_filterList = BookSerializer(book, many=True)  # 책 필터에 걸린 불러와서

        # print(book_filterList)
        # 랜덤으로 한개 추출
        # serializer = random.choice(book_filterList)

        # return Response(book_filterList.data)