Calibre FileType Plugin for Korean Text
==========================================
[Calibre](http://calibre-ebook.com) FileType Plugin that reformat Hangul(Korean) text

칼리버에서 한글 텍스트 파일을 읽어들일 때 포맷팅을 새로 하는 플로그인.

[epubia](https://code.google.com/p/epubia) 변환기의 입력단을 칼리버용 플러그인으로 재포장하였다.

## 기능
* 인코딩 자동변화 (EUC-KR을 UTF-8로 변환)
* [Markdown](http://scriptogr.am/myevan/post/markdown-syntax-guide-for-scriptogram) 지원
* 문단 재포맷. 자세한 형식은 [epubia](https://code.google.com/p/epubia/wiki/HangulText) 참고
* 줄바꿈으로 중간에 분리된 단어 추측
* 다음과 같은 줄을 챕터로 인식
  - 1
  - 제1장
  - 제1장. 챕터이름
  - 第一章

## 사용법
1. '파일 형식 플러그인' 항목에 Hangul Text Reformat 이라는 항목이 생겼는지 확인하고 옵션 설정
2. 설정 -> '변환하기/입력옵션' -> Text입력
  * 문단 스타일 **block**, 서식 스타일 **markdown** 으로 변경.
    기본값인 auto/auto로도 되어야 하는데 제대로 인식 못하는 경우가 있음.
3. 설정 -> '변환하기/공통옵션'  -> 목차
  * '1 수준 목차'을 **//h:h1** 로 지정
  * 섹션(##)까지 목차에 넣고 싶은 경우 '2 수준 목차'에 **//h:h2** 를 지정

## 옵션
* *Reformat* : 문단재포맷
* *Pretty Quote*  : " 을 열기/닫기 형태로 보기좋게 변환
* *Guess Chapter* : 챕터 자동 인식
* *Insert Empty Paragraph* : 연속된 빈줄을 문단간 띄기로 처리
* *Correct Word Break* : 줄간 분리된 단어 교정
