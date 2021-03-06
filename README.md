# ๐ Task CRUD ๊ธฐ๋ฅ ๊ตฌํ

## ๐ก ERD

<img width="642" alt="แแณแแณแแตแซแแฃแบ 2021-12-08 แแฉแแฎ 9 37 13" src="https://user-images.githubusercontent.com/73830753/145209562-4d915746-7965-489e-9578-01899ce567a0.png">

## ๐  ์ฌ์ฉ ๊ธฐ์  ๋ฐ ํด

> - Back-End : <img src="https://img.shields.io/badge/Python 3.8-3776AB?style=for-the-badge&logo=Python&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/MariaDB -003545?style=for-the-badge&logo=MariaDB&logoColor=white"/>
> - Deploy : <img src="https://img.shields.io/badge/Docker-0052CC?style=for-the-badge&logo=Docker&logoColor=white"/>
> - ETC : <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=Github&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=Swagger&logoColor=white"/>

## ๐ฉโ๐ป ๊ตฌํ ๊ธฐ๋ฅ

### MVP ํจํด ๊ตฌํ

View - Presenter - Model - Presenter - View

### users

- ์ ์ ์ ๋ํ ์ธ์ฆ(Authentication)์ ๊ณ ๋ คํ์ง ์์์ต๋๋ค.
- `/token` endpoint์ ์ ์ํ์ฌ db์ ์กด์ฌํ๋ ์ ์ ์ username, password๋ฅผ ์๋ ฅํ๋ฉด ํ ํฐ์ด ๋ฐ๊ธ๋ฉ๋๋ค.
- token์ ๋ฐ๊ธ๋ฐ์ ์ ์ ์ username๊ณผ password๋ฅผ authorizeํ๋ฉด task api์ ์ ๊ทผ์ด ๊ฐ๋ฅํฉ๋๋ค.

### tasks

- ์ ์ ์ ๊ถํ์ ํ์ธํ ํ ์ ์ ๋ task๋ฅผ Create, Read, Update, Delete ๊ธฐ๋ฅ์ ์ด์ฉ๊ฐ๋ฅํฉ๋๋ค.
  - ์ ์ ๋ user_id์ ํด๋นํ๋ task๋ฅผ ๋ชจ๋ ์ฝ์ ์ ์์ต๋๋ค.
  - ์ ์ ๋ ์๋ก์ด task๋ฅผ ์์ฑํ  ์ ์์ต๋๋ค.
  - ์ ์ ๋ user_id์ ํด๋นํ๋ ๋ชจ๋  task๋ฅผ ์ญ์ ํ  ์ ์์ต๋๋ค.
  - ์ ์ ๋ ํ๋์ ํน์  task๋ฅผ task_id๋ฅผ ์ง์ ํ์ฌ ์ญ์ ํ  ์ ์์ต๋๋ค.
  - ์ ์ ๋ ํ๋์ ํน์  task๋ฅผ ์์ ํ  ์ ์์ต๋๋ค.

## ๐ ์คํ ๋ฐฉ๋ฒ

๊ฐ์ํ๊ฒฝ ํ์ฑํ ํ ํฐ๋ฏธ๋์ ๋ฐ ๋ช๋ น์ด๋ฅผ ์๋ ฅํด์ฃผ์ธ์.

```
# ๋ก์ปฌ ๋๋ ํ ๋ฆฌ ์์ฑ
mkdir fastapi-crud && cd fastapi-crud
```

```
# ๋๋ ํ ๋ฆฌ ์์ ๊นํ๋ธ ๋ ํ์งํ ๋ฆฌ ํด๋ก 
git clone https://github.com/rimi0108/fastapi-crud.git .
```

```
# ํ์ ํจํค์ง ์ค์น
pip install -r requirements.txt
```

```
# ๋์ปค maridb ์ปจํ์ด๋ ์คํ
docker-compose up --build
```

```
# ํ๋ก์ ํธ ์๋ฒ ์คํ
uvicorn main:app --reload
```

```
# fastapi swagger์ ์ ์ํด ํต์  ํ์คํธ
http://127.0.0.1:8000/docs
```

๋ง์ง๋ง์ผ๋ก docker๋ก ๋์ด db์ ๋ฐ์ดํฐ๊ฐ ์ ๋ค์ด๊ฐ๋์ง ํ์ธํด์ฃผ์ธ์ ๐
