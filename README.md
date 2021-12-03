# 📍 Task CRUD 기능 구현

## 💡 ERD

<img width="801" alt="스크린샷 2021-11-18 오후 6 11 49" src="https://user-images.githubusercontent.com/73830753/142385765-3852e733-d441-45ed-9563-89e4a745e655.png">

## 🛠 사용 기술 및 툴

> - Back-End : <img src="https://img.shields.io/badge/Python 3.8-3776AB?style=for-the-badge&logo=Python&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=MariaDB&logoColor=white"/>
> - Deploy : <img src="https://img.shields.io/badge/Docker-0052CC?style=for-the-badge&logo=Docker&logoColor=white"/>
> - ETC : <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=Github&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white"/>

## 👩‍💻 구현 기능

### users

- 유저에 대한 인증(Authentication)은 고려하지 않았습니다.

### tasks

-

## 👀 실행 방법

1. 터미널을 이용하여 원하는 폴더에 들어가서 밑 명령어를 입력합니다.

```
git clone https://github.com/rimi0108/moneybook.git .
```

2. Docker 파일이 있는 위치에서 밑 명령어를 입력해 Docker 환경을 실행합니다.

```
docker-compose up --build
```

3. 서버 실행을 확인합니다.

```
django  | Starting development server at http://0.0.0.0:8000/
django  | Quit the server with CONTROL-C.
```

4. [Postman Docs](https://documenter.getpostman.com/view/16843855/UVCCeiac) 에 접속하여서

<img width="266" alt="스크린샷 2021-11-19 오후 6 54 50" src="https://user-images.githubusercontent.com/73830753/142603983-19bd6606-5b51-4791-bf2a-213852157d39.png">

우측 상단에 `Run in Postman` 버튼을 누르고 로그인 후 사용할 워크스페이스를 고릅니다.

<img width="269" alt="스크린샷 2021-11-19 오후 6 56 10" src="https://user-images.githubusercontent.com/73830753/142603629-0c9d5756-f7b0-4a11-a126-8fc55b6414ef.png">

<img width="265" alt="스크린샷 2021-11-19 오후 6 56 15" src="https://user-images.githubusercontent.com/73830753/142603640-f7e8d848-7d74-4e8c-8805-902cb97213cd.png">

포스트맨 환경을 No Environment에서 Local로 변경하고 통신을 시작합니다.

❗ mysql 한글 인코딩 에러 시

<img width="617" alt="스크린샷 2021-11-19 오후 8 49 48" src="https://user-images.githubusercontent.com/73830753/142618734-5531a954-6500-45ff-9439-db8573ab522f.png">

```
apt-get update
```

```
apt-get install vim
```

```
vim /etc/mysql/my.cnf
```

위 세가지 명령어를 mysql 컨테이너에서 실행합니다.

```
[client]
default-character-set=utf8

[mysql]
default-character-set=utf8

[mysqld]
collation-server = utf8_unicode_ci
init-connect='SET NAMES utf8'
character-set-server = utf8
```

my.cnf 파일에 위 코드를 추가합니다.

<img width="694" alt="스크린샷 2021-11-19 오후 9 01 41" src="https://user-images.githubusercontent.com/73830753/142619710-250c4d21-987f-4021-af25-9d7ceee57409.png">

정상적으로 한글이 뜨는 것을 확인하실 수 있습니다.

### unit test 실행법

1. Docker `django` 컨테이너에 접속하여 `manage.py`파일이 있는 위치에서 밑 명령어를 입력합니다.

```
python manage.py test
```

2. test 결과를 확인합니다.

```
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..............
----------------------------------------------------------------------
Ran 14 tests in 2.404s

OK
Destroying test database for alias 'default'...
```

위 화면은 test 성공 시 나오는 화면입니다.

❗ `Got an error creating the test database: (1044, "Access denied for user 'django'@'%' to database 'test_django'")`

위 에러 발생 시 mysql root에 접속하여

```
mysql> GRANT ALL PRIVILEGES ON test_django.* TO 'django'@'%';
```

```
mysql> FLUSH PRIVILEGES;
```

위 명령어를 입력해주세요.

## 🚀 Postman Docs
