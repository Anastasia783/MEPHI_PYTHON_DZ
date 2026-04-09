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

openrouter_api_key=sk-or-v1-ваш_ключ_здесь
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
<img width="1410" height="1027" alt="regisration full" src="https://github.com/user-attachments/assets/b3b40d68-7f6c-4528-90f5-689c4a57f8f1" />
<img width="1207" height="1023" alt="login" src="https://github.com/user-attachments/assets/7dc54f97-d20d-458b-a906-f48e485015dc" />
<img width="1253" height="933" alt="get_chat_history_after_delete" src="https://github.com/user-attachments/assets/355112b0-d74a-44b3-9149-a08f5631d611" />
<img width="1312" height="955" alt="get_chat_history" src="https://github.com/user-attachments/assets/d485a4f1-5ff2-4738-a6aa-d384afe5b6d9" />
<img width="1267" height="997" alt="get auth me" src="https://github.com/user-attachments/assets/db047831-0e87-4388-8777-630caf512e28" />
<img width="1328" height="882" alt="delete_chat_history" src="https://github.com/user-attachments/assets/2d08e05a-0526-41a5-97a7-2944bb540855" />
<img width="1287" height="932" alt="Chat_post" src="https://github.com/user-attachments/assets/7a2d20fb-252e-4c97-9c0e-6088c7a0518e" />
<img width="1138" height="842" alt="authorize" src="https://github.com/user-attachments/assets/863e6751-d587-479c-81d2-96b70218a8e0" />

