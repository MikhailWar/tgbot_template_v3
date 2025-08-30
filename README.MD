# Шаблон Telegram бота

## Описание
Шаблон проекта для создания Telegram бота с использованием архитектуры чистого кода (Clean Architecture), SQLAlchemy для работы с базой данных и Alembic для миграций.

## Структура проекта
```
tgbot_template_v3
├── src
│   └── app
│       ├── application    # Бизнес-логика приложения
│       │   ├── gateway    # Интерфейсы для работы с внешними сервисами
│       │   └── usecases   # Сценарии использования
│       ├── bootstrap      # Инициализация приложения
│       ├── domain         # Доменная модель
│       ├── infrastructure # Внешние сервисы и инфраструктура
│       └── presentation   # Слой представления
├── .env                   # Переменные окружения
├── .env.dist             # Шаблон переменных окружения
├── alembic.ini           # Конфигурация Alembic
└── requirements.txt      # Зависимости проекта
```

## Требования
- Python 3.11.5
- virtualenv

## Установка и настройка

1. Клонируйте репозиторий:
```bash
git clone <url_репозитория>
cd tgbot_template_v3
```

2. Создайте и активируйте виртуальное окружение:
```bash
python -m venv .venv

# Для Windows
.venv\Scripts\activate

# Для Linux/MacOS
source .venv/bin/activate
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Создайте файл с переменными окружения:
```bash
cp .env.dist .env
```

5. Отредактируйте файл `.env`, заполнив все необходимые поля.

## Настройка переменной окружения PYTHONPATH

В зависимости от используемой IDE или окружения, установите переменную PYTHONPATH:

### PowerShell (Windows):
```powershell
$env:PYTHONPATH = "$PWD/src"
```

### Bash (Linux/MacOS):
```bash
export PYTHONPATH=$PWD/src
```

### CMD (Windows):
```cmd
set PYTHONPATH=%CD%\src
```

## Настройка базы данных

1. Создайте начальную миграцию:
```bash
alembic revision --autogenerate
```

2. Примените миграции:
```bash
alembic upgrade head
```

## Запуск бота

```bash
python -m app.bootstrap.entrypoints.bot
```

## Разработка

При внесении изменений в модели данных не забывайте создавать и применять миграции:

```bash
alembic revision --autogenerate -m "описание изменений"
alembic upgrade head
```

## Лицензия
MIT