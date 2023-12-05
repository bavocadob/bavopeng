# BavoPeng
> 삼성 청년 SW 아카데미 (SSAFY) 10기 관통 PJT <br>
> 영화 추천 알고리즘 기반 커뮤니티 서비스 <br>
> 2023.11.16 ~ 2023.11.24

### TOC
1. [🤝TEAM](#🤝team)
2. [🛠️기술 스택](#🛠️기술-스택)
3. [🏷️역할분담](#🏷️역할분담)
4. [📐ERD](#📐erd)
5. [🎬Overview](#🎬overview)
    - [영화 추천](#영화-추천)
    - [영화 상세](#영화-상세)
    - [영화 리뷰](#영화-리뷰)
    - [커뮤니티](#커뮤니티)
    - [프로필](#프로필)
    - [네비게이션바](#네비게이션바)
    

## 🤝TEAM
|<img src="readme.assets/profileimg1.png" width="100">|<img src="readme.assets/profileimg2.png" width="100">|
|:--:|:--:|
|김해인(팀장)|강성은(팀원)|

## 🛠️기술 스택
### Tools
![vscode](https://img.shields.io/badge/vscode-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)
![Git Lab](https://img.shields.io/badge/gitlab-FC6D26?style=for-the-badge&logo=gitlab&logoColor=white)
![notion](https://img.shields.io/badge/notion-000000?style=for-the-badge&logo=notion&logoColor=white)
![mattermost](https://img.shields.io/badge/mattermost-0058CC?style=for-the-badge&logo=mattermost&logoColor=white)
![Figma](https://img.shields.io/badge/figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white)
![Postman](https://img.shields.io/badge/postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)


### Frontend
![vue.js](https://img.shields.io/badge/vue3-4FC08D?style=for-the-badge&logo=vuedotjs&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=HTML5&logoColor=white)
![CSS](https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=CSS3&logoColor=white)
![javascript](https://img.shields.io/badge/javaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Pinia](https://img.shields.io/badge/pinia-52CE63?style=for-the-badge&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAAC0AAAAtCAYAAAA6GuKaAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAfsSURBVFjD7Zl%2FjFxVFcc%2F572ZeTOzM7OzS4tAl7a0QimhUMsKFQRLQAyVQClUjE2srRWjkWgiJCQSMBHEHwkEJCRUpYA2YiM0YkJiE7EikkJsC1IjbSlCLaXYbnfb2fn53jvHP2bm7c7sEn69JfzhS25y77x77%2Fme7z33%2FHgD%2F386n9uG7i38aO8DvXHv60wV4B8euu%2B0dMPbSpanbhu6t%2FCRB337f%2B6a4ddts6%2BN%2BQ31FyWq7tc%2B8qCrZj%2Fz1Z%2FVCH189Wngr41zf4kb8E2v3rlCRDaKNLeXlhgxZ%2F6dp9z4chwyEnECvvHFG3sCDe5AWmxIBBlErgQ%2BfNDLd6y%2BnlA%2Ba8orjtmWx85dvxnB2u9r2ewXscapYuPAIk3swoK4yHnXoJc%2Fv3oOPvej5oqBmd28%2FG%2BrXuNpu%2BPxix75BYCvjbWYRCxH0AVMWfihg7Z6eIYgLgamIGagzDazny%2F745cv7p1WvKsR%2BIsnAB4bf6x7z8vvvdxLzes9XhJeamSOvLHllIdqMYO2eQiIAmaYAWpgIKpfqpRGP%2BOleqKr12Y4GoeWBFi2fllR0umvk5IlpJzLBMfBMfoPSG3581%2F93OPn%2FvLp2EBLQA%2BmHWAZ33eZEWhAh88YdxFN8K95%2BLqbTOxmU%2BtHpaW8gQlipDE9DYgPNKE2CCYB2%2BqHYmjog3Q4ugi8VcPpKvaTzuMDae%2FRxL4nVvOQmr1hqqBtIdbZTwpGUxEbcygROCv748bWatI8uabiIaY7YwXtVv0XAnFawlqCOia8wwb1sEOJSNl2U57ZdN4jQ7GG8SAMDhDoUMTue42tlS7QSnRSYoDqw7G7vE2rNg1d%2FasVL2Es6X6XTThcmEmwMJ1gwBUSAjWDQ6Hy93rI9krI4ap2mUzTPFADZd9wObFpSiKiOe6vJdQIdDElfH5mD1ecnMFzJlI9K%2BEy6LmEefhTCBv2lin5Os5EDBDM5J4tVz80MmUJ09WPrDgAcuKsXILvnd3LtLT7rtcON5TbXzjKv0s%2BOAIpgZSza99AbsG2wXX%2BlKWmDrJ2YX%2BKO87p6wRcPQrVLrKqI1AZjoZ9KYcfLCpy3nSPlo8JwsC%2B8F4Avy%2FQv7tk%2BsGbFvRqttuwUhkYPgDllgOoHYORg5Dq6bJ%2F4btn9nJGMWngrHni2t%2F8Y0rzaduzskC6dwfYHKL8c7yLqcOhvZApQLUE0%2BdC0ptUVMXXN7ME58jsdW9ObeWSyt2ChXMwbWZN2mrtsZuE7HFQGoKe%2FuZYrRU9taNlE3IiieSdU1q52KvfmIcTvIjgve3y%2BmjTRIonwrG3oPcESOcnzo26ohCeLyeve25qmJbGrZh6EbuqoGEngxrCtFng5aB%2FJmgwgeHohEzBQgfjtilh2t5cPZ2avY5JZuxGnQXeXGjsh8q2rjA5CavJEyCsgJY65wkNGpW5cuqG%2FfEyXQ2vQjUTMZW7gOde%2BxSXXnsP920MIX%2FJRPtuN%2Bkh6P82G585i23%2FXQm5C7pZT5Hw1sZvHmrXdYDKLmT37t2sXLmSG264gWMMdoEdZzbp03l2xzCFQoHBwUF27p8PpMfNCwG7LH7QYXhhJEQV%2FMPs27ePNWvWsHTpUgreEBM8irbmOnm2b9%2FO3XffDcBoNQBxuk9mnu1ZMT02m7adK2aSdF%2BPxmGa8sgVeB%2B%2FjNdGDjLjuCrZYw%2FiV9%2FirvUv851Vp%2BOlHJ7ccoClS2ZAosBw%2FmY2PPoEAwMDLLs4DYc2TBSf9BfJ7Ed3xJMwGeegGsnQIIl%2FJEv1r7vpcxzck%2F4AvQdJOsKVS07ixw%2F8k1CVTw8e32TRH6F36D5WLb6esBJyeMswuZNOJV3c1SnHdxYDMYEWZmBjmZmbGKZvzoNYmMFwcBKVyHHMn5Pj1m%2FOH3cXmjm0I%2FtI%2BI8h4TQSfTWSmTcYT0Sr8J0ZX2qqQa79pahDF6fcrAF1QsDoND4TwMj0bWsqJxIVhFGK2nx64gPtmqD2NrdAOvtmdCjYXmbyzldKcWNk2m9gDqpGGPgkPW9yodYGrpMEl655Ipgafr1KKpONSucYQTsjoIgZ5eFhMvk8XmYsMNbKZVKZDI7rjreJDpCNWhVxHJJeOvqtPNzMs1NeurkklCMx%2BulwJ6qIQL6vj8rRo9SrFTClWipRr1SaPKp2Bowo0BiO4zB65AhhowGmVI6OICi5YnHMtzvBizHWiMFOTHyMpOtCob%2FI6Mgx%2FGqNIAgo9BebH07bnxYisxgziUTCpdDXR2noMG4yiQjkin2taNj6fhXoS7ExLWdvLoP9pcmI4ToOqbRHvVYjk83itD6JdjS6sznFTbi4yQSNWo10Tw%2Ft%2FZrKhltl0ZOvx5x7BD9tH329VqVerZHvzVMtl2nUahMAdoToVr9SKqFBQE%2B%2Bh9GRo2gYtNKCEMTujz33kMGnNqO6FVMsVPKFLKmkSy6foVwqEzQaY3nJJIlTtVyhUa9TKBZIZ9Jksmk0aOXa2Auctfi3U1ME%2BPWrUHsl7SVwWyaRcB1yuTSjpTKm3Sw3ATdqdeq1GoXeXNP2NcRLJUm4DoT6FkF4jcj3deoK263nDYD3JNiC8UvNDHFk0u0supfSLXYrwlfkk3%2FeNaWFrSx%2Bbj9VZxFq3wLd0zaDyHt0mEezmJX2%2B%2FYJYC9jdgte8tL3A%2FgD%2FyVnz170CdDzQRchzpmYDSCWxsRBUKCKcQBjF47zL0L9Penabhnc5n8Quf8DA5tQI5aiLr8AAAAASUVORK5CYII%3D)
![Tailwind](https://img.shields.io/badge/tailwind-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)
<!-- ![Node.js](https://img.shields.io/badge/node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white) -->

### Backend
![Python](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

## 🏷️역할분담
|이름|역할|
|:--:|----|
|김해인<br>( BE, FE )|- ERD 설계<br> - Django ( accounts, articles )<br> - Vue ( 로그인, 회원가입, 프로필 )<br> - CSS<br> - ppt제작, 발표|
|강성은<br>( BE, FE )|- API 요청, DB 저장<br> - Django ( movies )<br> - Vue ( 영화, 리뷰, 게시글, 댓글, 검색 )<br> - 영화 추천 알고리즘<br> - CSS|

## 📐ERD
<img src="readme.assets/ERD.png" alt="ERD" width="900">

## 🎬Overview
### 영화 추천
|로그인|비로그인|
|:--:|:--:|
|<img src="readme.assets/recommand_movie_signin.png" alt="로그인 영화추천" width="450"><br><img src="readme.assets/recommand_movie_signin2.png" alt="로그인 영화추천" width="450">|<img src="readme.assets/recommand_movie.png" alt="비로그인 영화추천" width="450">|

<!-- |상태|화면|
|:--:|:--:|
|로그인|<img src="readme.assets/recommand_movie_signin.png" alt="로그인 영화추천" width="500"><br><img src="readme.assets/recommand_movie_signin2.png" alt="로그인 영화추천" width="500">|
|비로그인|<img src="readme.assets/recommand_movie.png" alt="비로그인 영화추천" width="500">| -->

### 영화 상세
|기본정보 / 스코어 / 커뮤니티 태그|줄거리 / 예고편 / 출연진|
|:--:|:--:|
|<img src="readme.assets/movie_detail.png" alt="영화상세" width="400"><br><img src="readme.assets/movie_detail3.png" alt="스코어" width="400"><br><img src="readme.assets/movie_detail4.png" alt="커뮤니티태그" width="400">|<img src="readme.assets/movie_detail2.png" alt="줄거리, 출연진" width="400">|

### 영화 리뷰
|내가 작성한 리뷰|전체 리뷰|리뷰 작성|
|:--:|:--:|:--:|
|<img src="readme.assets/my_review.png" alt="내 리뷰" width="280"><br><img src="readme.assets/my_review2.png" alt="내 리뷰" width="280">|<img src="readme.assets/review.png" alt="리뷰" width="270">|<img src="readme.assets/review_write.png" alt="리뷰 작성" width="250">|

<!-- |내용|화면||
|:--:|:--:|:--:|
|영화|<img src="readme.assets/movie_detail.png" alt="영화상세" width="300"><br><img src="readme.assets/movie_detail3.png" alt="스코어" width="300"><br><img src="readme.assets/movie_detail4.png" alt="커뮤니티태그" width="300">|<img src="readme.assets/movie_detail2.png" alt="줄거리, 출연진" width="300">|
|리뷰|<img src="readme.assets/my_review.png" alt="내 리뷰" width="300"><br><img src="readme.assets/my_review2.png" alt="내 리뷰" width="300">|<img src="readme.assets/review.png" alt="리뷰" width="290">|
|리뷰 작성|<img src="readme.assets/review_write.png" alt="리뷰 작성" width="250">|<img src="readme.assets/review_write2.png" alt="리뷰 수정" width="250">| -->

### 커뮤니티
|전체 게시글|게시글 상세|게시글 작성|
|:--:|:--:|:--:|
|<img src="readme.assets/community.png" alt="전체 게시글" width="280">|<img src="readme.assets/community_detail.png" alt="게시글 상세" width="270">|<img src="readme.assets/community_write.png" alt="게시글 작성" width="250">|

### 프로필
|내 프로필|프로필 수정|
|:--:|:--:|
|<img src="readme.assets/profile.png" alt="기본 정보" width="400"><br><img src="readme.assets/profile2.png" alt="기본 정보" width="400">|<img src="readme.assets/profile_modify.png" alt="프로필 수정" width="400">|

|팔로우 / 언팔로우|좋아하는 영화 / 보고싶은 영화|
|:--:|:--:|
|<img src="readme.assets/profile_other.png" alt="다른 사람" width="400"><br><img src="readme.assets/profile_other2.png" alt="다른 사람" width="400">|<img src="readme.assets/profile_movies.png" alt="좋아하는&보고싶은 영화" width="400"><br><img src="readme.assets/profile_movies2.png" alt="좋아하는&보고싶은 영화" width="400">|


### 네비게이션바
|로그인|비로그인|
|:--:|:--:|
|<img src="readme.assets/navbar_signin.png" alt="로그인 네브바" width="400"><br><img src="readme.assets/navbar2_signin.png" alt="로그인 네브바" width="400">|<img src="readme.assets/navbar.png" alt="비로그인 네브바" width="400"><br><img src="readme.assets/navbar2.png" alt="비로그인 네브바" width="400">|

