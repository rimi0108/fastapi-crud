# 📍 Task CRUD 기능 구현

## 💡 ERD

<img width="676" alt="스크린샷 2021-12-08 오전 3 51 01" src="https://user-images.githubusercontent.com/73830753/145088742-0eefe19a-8246-4859-90fd-2a4a2be2fd85.png">

## 🛠 사용 기술 및 툴

> - Back-End : <img src="https://img.shields.io/badge/Python 3.8-3776AB?style=for-the-badge&logo=Python&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/MariaDB 10-003545?style=for-the-badge&logo=MariaDB&logoColor=white"/>
> - Deploy : <img src="https://img.shields.io/badge/Docker-0052CC?style=for-the-badge&logo=Docker&logoColor=white"/>
> - ETC : <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=Github&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white"/>

## 👩‍💻 구현 기능

### users

- 유저에 대한 인증(Authentication)은 고려하지 않았습니다.
- `/token` endpoint에 db에 존재하는 유저의 username, password를 입력하면 토큰이 발급됩니다.
- token을 발급받은 유저의 username과 password를 authorize하면 task api를 사용 가능합니다.

### tasks

- 유저의 권한을 확인한 후 유저는 task를 Create, Read, Update, Delete 기능을 이용가능합니다.
  - 유저는 user_id에 해당하는 task를 모두 읽을 수 있습니다.
  - 유저는 task를 작성할 수 있습니다.
  - 유저는 user_id에 해당하는 모든 task를 삭제할 수 있습니다.
  - 유저는 하나의 특정 task를 task_id를 지정하여 삭제할 수 있습니다.
  - 유저는 하나의 특정 task를 수정할 수 있습니다.

## 👀 실행 방법
