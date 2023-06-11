# GPS_Toy_Project
A GPS Toy Project.

* requirements.txt에 있는 파이썬 라이브러리들(ex. django, djangorestframework... 등등) 부터 먼저 다운로드 받으세요. 참고로 제가 작업한 파이썬 버전은 3.8입니다. 아래 코드로 다운로드 받으실 수 있습니다.
  ```
  pip install -r requirements.txt
  ```
* runserver로 서버 실행 가능합니다.
  ```
  python manage.py runserver
  ```
* 이후 127.0.0.1:8000 으로 메인 페이지 접속 가능,
* 127.0.0.1:8000/admin으로 접속시 admin page 접속 가능(현재 계정은 아이디 : admin 패스워드 : adminpassword 입니다. 물론 db내용을 싹 삭제하시면 새롭게 정하실 수 있습니다.)
* 127.0.0.1:8000/update/으로 post 데이터 전송 가능.(주의! post할때 주소 마지막에 slash '/' 빠지면 오류남)

* db.sqlite3은 임시 데이터베이스입니다. 이 파일은 그냥 삭제하시고, 모든 디렉토리의 pycache 내용 다 삭제하고, 
* 아래의 코드들을 실행하면 전부 새롭게 만들어질테니 그렇게 하는게 나을 겁니다(무슨 말인지 모르겠다면 django 튜토리얼 part2.를 보세요.)
  ```
  python manage.py makemigrations myapp
  python manage.py migrate
  python manage.py createsuperuser
  ```
* django 튜토리얼 https://docs.djangoproject.com/ko/4.2/intro/tutorial01/
