# Telegram Monitor

**An asynchronous Telegram channel monitoring and keyword tracking application built with Python.**

Telegram Monitor tracks selected Telegram channels, searches incoming messages for configured keywords, and forwards relevant messages to the user's Telegram Saved Messages.

[English](#english) | [Русский](#русский)

---

# English

## Overview

Telegram Monitor is a Python application designed to monitor selected Telegram channels and automatically identify messages matching user-defined keywords.

Users can organize monitoring rules into separate settings, associate multiple channels with those settings, and receive notifications when relevant messages are found.

The project focuses on asynchronous processing, database-driven configuration, and modular backend architecture.

## Features

- **Telegram monitoring** - listen to new messages in selected Telegram channels using Telethon.
- **Keyword matching** - search incoming messages against configured keywords.
- **Multiple monitoring configurations** - organize keywords and channels into separate settings.
- **Channel management** - associate Telegram channels with monitoring configurations.
- **Message notifications** - forward matching messages to Telegram Saved Messages.
- **REST API** - manage application resources through FastAPI endpoints.
- **Asynchronous database operations** - use SQLAlchemy's async API for database access.

## Tech Stack

Python      - Core application
FastAPI     - REST API
Telethon    - Telegram client and event handling
SQLAlchemy  - ORM and database access
SQLite      - Database
Pydantic    - Data validation and schemas
asyncio     - Asynchronous processing
Git         - Version control

## Architecture

The application follows a layered architecture with separation between API, business logic, data access, and Telegram integration.

app/
├── db/
│   ├── models/
│   └── repositories
├── services/
├── schemas/
├── web/
│   └── api.py
├── telegram/
│   ├── handlers/
│   ├── channels/
│   └── ...
├── dependencies.py
tests

**Main architectural components:**

- **API layer** - handles HTTP requests through FastAPI.
- **Service layer** - implements business logic and coordinates operations.
- **Repository layer** - encapsulates database queries and persistence.
- **Telegram integration** - manages the Telegram client, event handlers, and message processing.
- **Dependency composition** - centralizes application component creation and dependency injection.

## How It Works

1. The application connects to Telegram through Telethon.
2. Monitoring configurations are loaded from the database.
3. Event handlers are registered for selected channels.
4. When a new message arrives, the handler retrieves the corresponding monitoring configuration.
5. The message is checked against active keywords.
6. Matching messages are forwarded to Telegram Saved Messages.

## Getting Started

### Requirements

- Python 3.13+
- Telegram API credentials
- Telegram account

### Installation

Clone the repository:

```bash
git clone <repository-url>
cd telegram-monitor
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux / macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -e .
```

### Configuration

Create a `.env` file in the project root and provide your Telegram API credentials.

```env
TELEGRAM_API_ID=your_api_id
TELEGRAM_API_HASH=your_api_hash
```

The exact environment variable names should match the application's configuration.

You can obtain Telegram API credentials at [my.telegram.org](https://my.telegram.org).

### Running the Application

Start the FastAPI application using your configured ASGI entry point.

For example:

```bash
uvicorn app.web.api:app --reload
```

On the first run, Telethon may request a Telegram login code to authorize the account.

## Project Status

The project is under active development.

### Planned Improvements

- User authentication and authorization.
- Multiple notification recipients.
- Improved monitoring configuration management.
- More robust Telegram connection and reconnection handling.
- Automated tests.
+ Database migrations with Alembic.
- Docker support.

## License

This project is currently developed as a personal portfolio project.

---

# Русский

## О проекте

Telegram Monitor — приложение на Python для мониторинга выбранных Telegram-каналов и автоматического поиска сообщений по заданным ключевым словам.

Пользователь может создавать отдельные конфигурации мониторинга, привязывать к ним каналы и ключевые слова, а также получать уведомления, когда в новых сообщениях обнаруживаются совпадения.

Проект ориентирован на асинхронную обработку событий, конфигурацию через базу данных и модульную архитектуру backend-приложения.

## Возможности

- **Мониторинг Telegram-каналов** — отслеживание новых сообщений с помощью Telethon.
- **Поиск по ключевым словам** — проверка входящих сообщений на соответствие заданным ключевым словам.
- **Несколько конфигураций мониторинга** — возможность разделять каналы и ключевые слова по отдельным настройкам.
- **Управление каналами** — привязка Telegram-каналов к конфигурациям мониторинга.
- **Уведомления** — пересылка найденных сообщений в Избранное Telegram.
- **REST API** — управление ресурсами приложения через FastAPI.
- **Асинхронная работа с БД** — использование асинхронного API SQLAlchemy.

## Технологический стек

Python      - Основной язык
FastAPI     - REST API
Telethon    - Работа с Telegram и обработка событий
SQLAlchemy  - ORM и взаимодействие с БД
SQLite      - База данных 
Pydantic    - Валидация данных и схемы
asyncio     - Асинхронная обработка
Git         - Контроль версий

## Архитектура

Проект использует многоуровневую архитектуру с разделением API, бизнес-логики, доступа к данным и интеграции с Telegram.

app/
├── db/
│   ├── models/
│   └── repositories
├── services/
├── schemas/
├── web/
│   └── api.py
├── telegram/
│   ├── handlers/
│   ├── channels/
│   └── ...
├── dependencies.py
tests

**Основные компоненты:**

- **API layer** - обработка HTTP-запросов через FastAPI.
- **Service layer** - бизнес-логика и координация операций.
- **Repository layer** - запросы к базе данных и сохранение данных.
- **Telegram integration** - управление Telegram-клиентом, обработчиками событий и обработкой сообщений.
- **Dependency composition** - централизованное создание компонентов приложения и внедрение зависимостей.

## Принцип работы

1. Приложение подключается к Telegram через Telethon.
2. Из базы данных загружаются конфигурации мониторинга.
3. Для выбранных каналов регистрируются обработчики событий.
4. При поступлении нового сообщения обработчик получает соответствующую конфигурацию.
5. Сообщение проверяется на совпадения с активными ключевыми словами.
6. Если найдены совпадения, сообщение пересылается в Избранное Telegram.

## Установка и запуск

### Требования

- Python 3.13+
- API credentials Telegram
- Аккаунт Telegram

### Установка

Клонировать репозиторий:

```bash
git clone <repository-url>
cd telegram-monitor
```

Создать и активировать виртуальное окружение:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux / macOS:

```bash
source .venv/bin/activate
```

Установить зависимости:

```bash
pip install -e .
```

### Настройка

Создать файл `.env` в корне проекта и указать API credentials Telegram.

```env
TELEGRAM_API_ID=your_api_id
TELEGRAM_API_HASH=your_api_hash
```

Названия переменных должны соответствовать конфигурации приложения.

Получить API credentials можно на [my.telegram.org](https://my.telegram.org).

### Запуск

Запустить FastAPI-приложение через настроенную ASGI-точку входа.

Например:

```bash
uvicorn app.web.api:app --reload
```

При первом запуске Telethon может запросить код авторизации Telegram.

## Статус проекта

Проект находится в активной разработке.

### Планы по развитию

- Аутентификация и авторизация пользователей.
- Поддержка нескольких получателей уведомлений.
- Развитие управления конфигурациями мониторинга.
- Улучшение обработки ошибок подключения и переподключения к Telegram.
- Автоматизированные тесты.
+ Миграции базы данных с Alembic.
- Поддержка Docker.

## Лицензия

Проект разрабатывается в качестве личного портфолио.
