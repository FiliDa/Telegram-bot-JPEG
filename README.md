# 🐾 Varty Bot — Telegram контент‑бот на aiogram 3

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![aiogram](https://img.shields.io/badge/aiogram-3.x-2CA5E0?style=flat&logo=telegram&logoColor=white)](https://docs.aiogram.dev/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)](https://www.sqlite.org/)

Легкий и быстрый Telegram‑бот для раздачи медиа по категориям, ведения базы пользователей и управления рассылками. Хранит состояние рассылок в базе, поддерживает остановку активных задач и удобную конфигурацию через переменные окружения.

## 💡 Возможности

- Категории контента с кнопками (см. набор в [config.py](file:///e:/GITR — копия/varty_bot/config.py)).
- Сбор и учет пользователей (таблица `users` в [database.py](file:///e:/GITR — копия/varty_bot/database.py)).
- Массовые рассылки c прогрессом и статусами (`broadcast_jobs`). 
- Быстрая остановка активных задач: [admin_stop_jobs.py](file:///e:/GITR — копия/varty_bot/admin_stop_jobs.py).
- Переменные окружения через `.env` (поддерживается `python-dotenv`).
- Проверка наличия токена: [check_token.py](file:///e:/GITR — копия/varty_bot/check_token.py).
- Автоперезапуск под Windows: [run_forever.ps1](file:///e:/GITR — копия/varty_bot/run_forever.ps1).

## 🧱 Архитектура данных

База `SQLite` создается автоматически (см. [database.py](file:///e:/GITR — копия/varty_bot/database.py)):

- `users(user_id, username, join_date)` — учет аудитории.
- `broadcast_jobs(id, audience, media_file_id, media_type, caption, status, offset, total, source, created_at, updated_at)` — задачи рассылок с прогрессом.

## 🗂 Структура проекта

```
varty_bot/
├── config.py           # Конфигурация и категории
├── database.py         # Модель данных (aiosqlite)
├── admin_stop_jobs.py  # Остановка активных рассылок (SQLite)
├── check_token.py      # Быстрая проверка BOT_TOKEN
├── run_forever.ps1     # Автоперезапуск (Windows)
├── requirements.txt    # Зависимости
├── bot_database.db     # База (создается автоматически)
└── media/              # Папки с контентом (см. CATEGORIES в config.py)
```

Категории → директории задаются в `CATEGORIES` ([config.py](file:///e:/GITR — копия/varty_bot/config.py)) — просто положите файлы в соответствующие подпапки внутри `media/`.

## ⚙️ Установка

1. Установите Python 3.10+
2. Установите зависимости:

```bash
pip install -r requirements.txt
```

3. Создайте `.env` в корне `varty_bot`:

```env
BOT_TOKEN=your_telegram_bot_token_here
ADMIN_ID=123456789          # ваш Telegram ID (администратор)
CHANNELS=-1001111111111,-1002222222222   # список каналов через запятую
```

> Важно: значения `ADMIN_ID` и `CHANNELS` теперь берутся из окружения (см. [config.py](file:///e:/GITR — копия/varty_bot/config.py)).

## 🚀 Запуск

- Быстрый старт (Windows):

```powershell
python .\\check_token.py
python .\\main.py
# или с автоперезапуском
.\run_forever.ps1
```

- Linux/macOS:

```bash
python3 check_token.py
python3 main.py
```

## 🧰 Управление рассылками

- Остановить все активные задачи:

```bash
python admin_stop_jobs.py
```

Скрипт проставит `status='stopped'` для всех `running` задач и покажет короткий отчет.

## 🛡 Рекомендации по безопасности

- Не коммитьте `.env`, базу `bot_database.db` и списки пользователей.
- Добавьте `.gitignore` с исключениями: `.env`, `*.db`, `*oldUsers*.json`, `__pycache__/`.
- Никогда не храните токены и ID в коде — используйте переменные окружения.

## 🧩 Зависимости

Список — в [requirements.txt](file:///e:/GITR — копия/varty_bot/requirements.txt):

- `aiogram>=3.0.0`
- `python-dotenv`
- `aiosqlite`

## 👤 Автор

Filippov D.A. — Backend Engineer (Telegram Bots, Python)

- Email: phoenixmediacall@gmail.com
- Telegram: @filippov_da
- GitHub: https://github.com/FiliDa

---

Если проект полезен — поставьте ⭐ на GitHub и поделитесь обратной связью.
*** End Patch***} ***!
