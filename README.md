## Chat API
Серверное приложение на FastAPI, предоставляющее защищённый API для взаимодействия с большой языковой моделью (LLM) через сервис OpenRouter.
В рамках задания реализована  аутентификация и авторизация пользователей с использованием JWT, хранение данных в базе SQLite, а также корректно разделена ответственность между слоями приложения (API, бизнес-логика, доступ к данным).

## Требования

- Python 3.12 или выше
-
### Установка uv 

 pip install uv
  

После установки проверь:

uv --version


## Проект

### Клонировать репозиторий

git clone https://github.com/Anastasia783/MEPHI_PYTHON_DZ.git
cd MEPHI_PYTHON_DZ


### Установить зависимости через uv

uv sync


## Настройка

### Создать файл `.env` в корне проекта

app_name=llm-p
env=local

jwt_secret=change_me_super_secret
jwt_alg=HS256
access_token_expire_minutes=60

sqlite_path=./app.db

openrouter_api_key=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
openrouter_base_url=https://openrouter.ai/api/v1
openrouter_model=mistralai/mistral-7b-instruct:free
openrouter_site_url=https://example.com
openrouter_app_name=llm-fastapi-openrouter
openrouter_timeout=30


### Как получить ключ OpenRouter

1. Зарегистрируйся на https://openrouter.ai
2. Перейди в раздел GET Key
3. Скопируй ключ 
4. Вставь его в .env в openrouter_api_key

## Запуск

uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

 ## Открыть Swagger 
 http://127.0.0.1:8000/docs

 ## Структура проекта

 app/
|---- api/
│ |- deps.py
│ |-routes_auth.py #
│ |-routes_chat.py
|---- core/
| |- config.py 
| |-errors.py 
│ |- security.py 
|- db/
│ |- base.py 
│ |-models.py 
│ |- session.py 
|-- repositories/
│ |- users.py # Репозиторий пользователей
|-- schemas/
│ |- auth.py # Схемы авторизации
│ |- chat.py # Схемы чата
│ |-user.py # Схема пользователя
|-- services/
│ |-openrouter_client.py # Клиент OpenRouter API
├── usecases/
│ |- auth.py # Бизнес-логика авторизации
│ |-chat.py # Бизнес-логика 
|-- main.py 

## Использование через Swagger

1. Открой `http://127.0.0.1:8000/docs
2. Зарегистрируй пользователя через POST /auth/register
3. Войди через POST /auth/login и получи access_token
4. Нажми Authorize в правом верхнем углу
5. Введи username и password в форму авторизации
6. Теперь все защищённые эндпоинты доступны

## Скриншоты работы API в screen

regisration full.png
login.png
authorize.png
get auth me.png
Chat_post.png
get_chat_history.png
delete_chat_history.png
 get_chat_history_after_delete.png

