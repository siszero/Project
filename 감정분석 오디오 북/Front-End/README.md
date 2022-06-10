# anaconda 설치
## 가상환경 생성

1. conda 가상환경 생성
```
conda create --name [가상환경 이름]
```

2. 특정 python version의 conda env 생성
```
conda create -n [가상환경 이름] python=3.10
```

3. conda 가상환경 조회
```
conda env list
```

4. 가상환경 실행
```
conda activate [가상환경 이름]
```

5. 가상환경 종료
```
conda deactivate
``` 

6. conda 가상환경 제거(remove)
```
conda remove --name [가상환경 이름] --all
```


# Django 설치

1. pycharm 들어가서 아무 프로젝트나 생성하기
2. 터미널 열기
3. cd ../ 로 PycharmProjects로 나오기
4. pip install django
5. django REST framework 패키지를 설치
```
pip install django djangorestframework
```
6. django-admin startproject [원하는 프로젝트 명]
7. [File] - [Open] - [생성한 프로젝트 명]
8. 코드 작성
9. terminal에서 migration하기
```
python manage.py makemigrations
python manage.py migrate
```

10. 서버 실행
```
python manage.py runserver
# 실행 시 나오는 주소 '127.0.0.1:8000' 클릭
# 로켓이 날라가는 화면이 브라우저에 나타나면 성공
```


[출처](https://ffoorreeuunn.tistory.com/287)
