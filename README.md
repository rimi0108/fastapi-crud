# 📍 Task CRUD 기능 구현

## 💡 ERD

<img width="642" alt="스크린샷 2021-12-08 오후 9 37 13" src="https://user-images.githubusercontent.com/73830753/145209562-4d915746-7965-489e-9578-01899ce567a0.png">

## 🛠 사용 기술 및 툴

> - Back-End : <img src="https://img.shields.io/badge/Python 3.8-3776AB?style=for-the-badge&logo=Python&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/MariaDB -003545?style=for-the-badge&logo=MariaDB&logoColor=white"/>
> - Deploy : <img src="https://img.shields.io/badge/Docker-0052CC?style=for-the-badge&logo=Docker&logoColor=white"/>
> - ETC : <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=Github&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=Swagger&logoColor=white"/>

## 👩‍💻 구현 기능

### MVP 패턴 구현

View - Presenter - Model - Presenter - View

### users

- 유저에 대한 인증(Authentication)은 고려하지 않았습니다.
- `/token` endpoint에 접속하여 db에 존재하는 유저의 username, password를 입력하면 토큰이 발급됩니다.
- token을 발급받은 유저의 username과 password를 authorize하면 task api에 접근이 가능합니다.

### tasks

- 유저의 권한을 확인한 후 유저는 task를 Create, Read, Update, Delete 기능을 이용가능합니다.
  - 유저는 user_id에 해당하는 task를 모두 읽을 수 있습니다.
  - 유저는 새로운 task를 생성할 수 있습니다.
  - 유저는 user_id에 해당하는 모든 task를 삭제할 수 있습니다.
  - 유저는 하나의 특정 task를 task_id를 지정하여 삭제할 수 있습니다.
  - 유저는 하나의 특정 task를 수정할 수 있습니다.

## 🚀 실행 방법

가상환경 활성화 후 터미널에 밑 명령어를 입력해주세요.

```
# 로컬 디렉토리 생성
mkdir fastapi-crud && cd fastapi-crud
```

```
# 디렉토리 안에 깃허브 레파지토리 클론
git clone https://github.com/rimi0108/fastapi-crud.git .
```

```
# 필요 패키지 설치
pip install -r requirements.txt
```

```
# 도커 maridb 컨테이너 실행
docker-compose up --build
```

```
# 프로젝트 서버 실행
uvicorn main:app --reload
```

```
# fastapi swagger에 접속해 통신 테스트
http://127.0.0.1:8000/docs
```

마지막으로 docker로 띄운 db에 데이터가 잘 들어갔는지 확인한다.
