from django.db import models

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)

class Book(models.Model):
    # objects = models.Manager()
    id = models.IntegerField(primary_key=True)  # 책 ID
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    writer = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)
    # image = models.CharField(max_length=10)
    image = models.CharField(max_length=10, null=True, default='')

class Music(models.Model):
    id = models.IntegerField(primary_key=True)  # 배경음악 ID
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=50)

class RecommendedBook(models.Model):
    # objects = models.Manager()
    id = models.IntegerField(primary_key=True)  # 책 ID
    title = models.CharField(max_length=50)
    writer = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)
    image = models.CharField(max_length=10, null=True, default='')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  # 책이 지워질 때 이에 대한 추천 책들도 지워지도록 하기 위함

