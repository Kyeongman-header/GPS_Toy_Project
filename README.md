# GPS_Toy_Project
A GPS Toy Project.

* Requirements.txt에 있는 파이썬 라이브러리들(ex. django, djangorestframework... 등등) 부터 먼저 다운로드 받으세요 ->
*  pip install -r requirements.txt
참고로 제가 작업한 파이썬 버전은 3.8입니다.

* 실행 -> python manage.py runserver
이후 127.0.0.1:8000 으로 메인 페이지 접속 가능,
127.0.0.1:8000/admin으로 접속시 admin page 접속 가능(계정은 아이디 : admin 패스워드 : adminpassword 입니다.)

* sqlite은 임시 데이터베이스입니다. 그냥 삭제하시고, 모든 디렉토리의 pycache 내용 다 삭제하고, 새롭게 migrate하면 전부 새롭게 만들어질테니 그렇게 하는게 그냥 나을 겁니다
* django 튜토리얼 https://docs.djangoproject.com/ko/4.2/intro/tutorial01/
