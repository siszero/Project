# 구글 플레이 스토어 웹 크롤링

> jupyter notebook 사용

1. 크롬 설치


  [설치](https://www.google.com/chrome/?brand=BNSD&gclid=Cj0KCQjwwNWKBhDAARIsAJ8Hkhf4pbUYQpGAE5BNOejRRmM17KWFaVmDkWzGVpfFsqsOoVVZgW8UYSIaAmlTEALw_wcB&gclsrc=aw.ds)



2. 크롬 버전 확인    
![](https://user-images.githubusercontent.com/64197543/161762861-f1b10db8-d6a1-4f86-b53d-127b03e95349.PNG)    
[⋮] - [도움말] - [Chrome 정보]



3. 크롬 드라이버 설치
- 버전에 맞는 크롬 드라이버 설치 (Window, Linux, Mac - 이 때, Window64여도 Window32 다운받으면 됨)



4. playstore-review-crawler-master 폴더 안에 다운받은 chromedriver 파일 넣기
- linux로 다운받으면 파일이 chromedriver
- window로 다운받으면 파일이 chromedriver.exe



5. 패키지 설치
- beatuiful soup: HTML/XML 문서 parsing
- selenium: 브라우저 동작 자동 제어
- pandas: 데이터 분석 라이브러리
- tqdm: 작업 프로세스 바(progress bar) 시각화

```
pip install beautifulsoup
pip install selenium
pip install pandas
pip install tqdm
```



6. playstore-review-crawler-master 폴더 안의 crawler 코드 실행



[참고](https://heytech.tistory.com/293)
