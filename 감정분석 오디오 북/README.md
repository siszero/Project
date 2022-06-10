# 감정 분석을 이용한 사용자 맞춤 오디오북, "내 마음을 읽어줘"

## ◼ 기간
2022.04 - 2022.04

## ◼ 팀원
6명

## ◼ 성과
AI 프로젝트 장려상(POSCO 청년 AI Big Data 아카데미)

## ◼ 개요
✔ 본 프로젝트의 부제는 "내 마음을 읽어줘"로 단순 오디오북이 아닌 사용자의 감정을 인식하여
책을 읽어주는 기능을 구현하였다. "마음을 알아준다"와 "책을 읽어준다"라는 중의적 의미를 담고
있으며 사용자에 맞춤형 책을 추천하고 읽어줌으로써 우울 또는 힐링을 필요로 하는 현대인들을
위로하고자 한다.

## 차별성
✔ 아직 데이터가 적어 아직 4가지 감정만을 분류하고 있지만 STT(Speech to Text)를
통해 간편하게 그날 그날의 감정을 간편하게 분석해 도서를 추천하며 바쁜 현대인에 맞춰 이를
읽어준다는 것에서 의미를 갖는다.   

✔ 단지 오디오북의 서비스를 제공하는 것이 아닌, 사용자의 마음을 읽고 그에 맞는 도서를
추천, 읽어줌으로써 그저 '독서'라는 기능에서 벗어나 위안, 나아가 심리치료의 영역에서도 적용
가능할 아이디어이자 서비스를 제공하기에 기존의 사례들과 차별화되어 있다고 할 수 있다


## ◼ 구현
1. 웹 스크래핑(Wep Scraping)
2. WordCloud
3. 감정분석(KoBERT모델)
4. 추천 알고리즘(콘텐츠 기반 필터링)
5. 음성합성(Tacotron)
6. FrontEnd(Android Studio)
7. BackEnd(Django)
8. DataBase(MySQL)

## ◼ 시나리오
![](https://user-images.githubusercontent.com/64197543/173026991-e2771c6a-76f3-4f57-bc59-400c9b6b9038.JPG)


## ◼ 시스템 구성도
![](https://user-images.githubusercontent.com/64197543/173026988-cf6a3c53-d125-4aa9-be6c-bfa2b91c4b38.JPG)

## ◼ 기술스택
<img src="https://user-images.githubusercontent.com/64197543/173026299-c55ff20b-9df1-47fa-bc17-cec08ead4366.png" width="600" height="250"/>



## ◼ 참고 자료

[1] 백재현. “SNS 감정분석을 통한 맞춤형 노래 추천 인공지능 스피커”. 동국대학교 대학원

[2] SKTBrain KoBERT, https://github.com/SKTBrain/KoBERT

[3] 다중감정 분류 모델 구현, https://hoit1302.tistory.com/159#1.BERT,KoBERT%EB%9E%80?

[4] KoBERT finetuning 코드, https://github.com/SKTBrain/KoBERT/blob/master/scripts/NSMC/naver_review_classifications_p
ytorch_kobert.ipynb

[5] 웹 스크래핑, https://zzsza.github.io/development/2019/03/12/crawling-in-developer-tools-console/

[6] 웹 스크래핑, https://blog.naver.com/codingteacher/222319094945

[7] 워드 클라우드, https://blog.naver.com/yk02061/222262810714

[8] 워드 클라우드, https://terms.naver.com/entry.naver?docId=6210350&cid=42346&categoryId=42346

[9] 추천 알고리즘, https://github.com/keyhong/contents_based_filtering-TF-IDF음성합성

[10] Tacotron: Towards End-to-End Speech Synthesis (Yuxuan Wang, RJ Skerry-Ryan, Daisy Stanton, Yonghui Wu, Ron J. Weiss, Navdeep Jaitly, Zongheng Yang, Ying Xiao, Zhifeng Chen, Samy Bengio, Quoc Le, Yannis Agiomyrgiannakis, Rob Clark, Rif A. Saurous)

[11] 조수희. "딥러닝 기반 보코더의 음성 합성에 대한 음성학적 관찰." 국내석사학위논문 고려대학교 대학원, 2020. 서울

[12] https://github.com/chldkato/Tacotron-Korean

[13] https://github.com/chldkato/Tacotron-pytorch

[14] https://github.com/carpedm20/multi-speaker-tacotron-tensorflow

[15] oecd 우울증 이상서, 말할 수 없는 우울증...내 속은 곪아간다, 연합뉴스, 2018.08.18, https://www.yna.co.kr/view/AKR20180816166700797