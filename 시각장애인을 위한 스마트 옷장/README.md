# smartCloset
## ◼ 개요
✔ 시각장애인의 90.3%는 질환과 사고로 인한 후천적인 원인으로 장애가 발생

✔ 장소, 시간, 목적에 따라 자유롭게 옷을 골라 입고 싶은 욕구가 있지만 옷의 촉감과 기억에만 의존하기 때문에 어려움이 있다.
## ◼ 목표
✔ 시각장애인의 독립적인 의생활을 지원

✔ 옷에 대한 패턴, 색상과 같은 시각적인 정보를 분류

✔ 사용자의 음성을 인식하여 옷에 대한 시각적인 정보를 음성 정보로 전달
## ◼ 기능
✔ 서버에서 사용자의 옷의 패턴을 판단하여 음성으로 출력해준다.
- 옷의 패턴은 무지, 스트라이프. 땡땡이, 체크, 그래픽인 5가지로 분류한다.
- 사용자의 요청으로 촬영된 옷의 패턴을 파악하여 사용자에게 음성데이터로 패턴 정보에 대해 알려준다.

✔ 사용자의 옷의 색상을 판단하여 음성으로 출력해준다.
- 옷의 색상은 빨간색, 주황색, 노란색, 초록색, 파란색, 남색, 보라색, 갈색, 회색, 검은색, 흰색인 12가지로 분류한다.
- 사용자의 요청으로 촬영된 옷의 색상을 파악하여 사용자에게 음성데이터로 색상 정보에 대해 알려준다.

✔ 사용자의 편의를 위한 각종 센서 장착 (아두이노와 라즈베리파이 사용)
- 인체감지센서가 사용자를 인식하면 옷장 손잡이에 붙어 있는 LED가 작동
- 마그네틱센서와 블루투스 통신을 통해 문열림 상태에 따라 스피커 ON/OFF 설정
- 습도센서와 쿨링팬을 이용하여 옷장 내부의 습도를 조절
## ◼ 구현
1. Google Image Crawling을 이용한 데이터 수집
2. labelImg를 이용한 데이터 라벨링
3. cuDNN과 SSD MobileNet V2 모델을 이용하여 패턴 관련 학습 데이터 생성
4. 학습 데이터를 통해 실시간으로 객체를 분류하는 코드 작성
5. 유클라디언 거리 공식을 이용한 색상 분류 코드 작성
6. TTS와 STT를 위한 gtts 모듈 사용
7. 각종 센서 부착 및 코드 작성과 블루투스 통신 코드 작성

## ◼ 시나리오
<img src="https://user-images.githubusercontent.com/64197428/147849202-c7dc6414-57af-46b1-9eea-905b7cb5314d.png" width=70% height = 70%>
<img src="https://user-images.githubusercontent.com/64197428/147849244-c0e9ef24-ef6e-4cdb-a4f8-b9b3bf9f9e4f.png" width=70% height = 70%>

## ◼ 시스템 구성도
<img src="https://user-images.githubusercontent.com/64197428/147849506-9eafd93e-acee-4882-813d-9a137a092fc1.png" width=70% height = 70%>

## ◼ 참고 자료

[1] FPN, https://herbwood.tistory.com/18

[2] "시각장애인이라고 장례식서 빨간 옷 입을 순 없죠.",  https://www.hankookilbo.com/News/Read/A2020121013120000624

[3] 당신도 어느날 갑자기 안 보일 수 있다…후천성이 90% , 
https://www.hani.co.kr/arti/society/society_general/558762.html

[4] 김태미, 조철현, “시각장애인의 의복행동에 대한 질적 연구”, 복식문화학회, p.82, 2016

[5] https://www.youtube.com/watch?v=yqkISICHH-U


## 기간
2021.03 - 2021.07

## 팀원
2명

## 성과
2021 KOREATECH 졸업작품 경진대회 장려상

## 기술스택
<img src="https://user-images.githubusercontent.com/64197543/172870834-8be98443-3629-40ec-8856-c12180e8b71b.png" width="600" height="250"/>
