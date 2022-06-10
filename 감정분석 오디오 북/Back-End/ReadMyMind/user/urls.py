from django.urls import path
from . import views

app_name = 'user'

urlpatterns=[
    path('user', views.user_getAll, name='user_getAll'),
    # 한권만
    path('book/<int:id>', views.book_selectOne, name="book_selectOne"),
    # 랜덤 추천
    # path('book/<str:emotion>', views.book_selectOne, name="book_selectOne"),  # angry/sad/happy/peace

    path('music/<str:emotion>', views.music_selectOne, name="music_selectOne"),
    path('recommendedbook/<int:book_pk>', views.book_recommend, name="book_recommend")
]

# path('randombook/<str:emotion>', views.book_random, name="book_random"),