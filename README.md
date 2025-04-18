# Vehicle Monitoring System

Це система для моніторингу транспортних засобів, побудована на фреймворку Django з використанням бази даних PostgreSQL. Система дозволяє здійснювати операції CRUD для компаній та транспортних засобів. Для зберігання даних використовується PostgreSQL, який піднімається через Docker.

## Опис проекту

- **Мова програмування:** Python  
- **Фреймворк:** Django  
- **База даних:** PostgreSQL  
- **Контейнеризація:** Docker  
- **Тести:** pytest  

## Початок роботи

### Вимоги

Перед тим, як запустити проект, переконайтесь, що у вас встановлені наступні інструменти:

- Python 3.x  
- Docker  
- Docker Compose  
- Poetry  

### Запуск проекту

#### 1. Клонування репозиторію

Спочатку клонувати репозиторій на свою локальну машину:

```bash
git clone <https://github.com/Le0n-K/vehicle-monitoring-system.git>
cd vehicle-monitoring-system
```

#### 2. Налаштування середовища

Створіть віртуальне середовище за допомогою Poetry:

```bash
poetry install
```

#### 3. Підйом контейнерів Docker

##### Для MacOS / Linux:

Створіть файл `.env` для налаштування змінних середовища (наприклад, підключення до бази даних):

```bash
DATABASE_URL=postgres://user:password@localhost:5432/postgres
```

Запустіть Docker контейнер з PostgreSQL:

```bash
docker-compose up -d
```

##### Для Windows:

Створіть файл `.env` для налаштування змінних середовища (аналогічно):

```bash
DATABASE_URL=postgres://user:password@localhost:5432/postgres
```

Запустіть Docker контейнер:

```bash
docker-compose up -d
```

#### 4. Міграції

Після підняття контейнерів, виконайте міграції для створення бази даних:

```bash
python manage.py migrate
```

#### 5. Створення суперкористувача

Щоб мати доступ до адміністративної панелі Django, створіть суперкористувача:

```bash
python manage.py createsuperuser
```

#### 6. Запуск сервера

Тепер можна запустити сервер:

```bash
python manage.py runserver
```

Відкрийте браузер і перейдіть за адресою http://127.0.0.1:8000/.

#### 7. Запуск тестів

Для запуску тестів використовуйте команду:

```bash
pytest
```

## Технічні деталі

- **Django:** Для створення веб-застосунку  
- **PostgreSQL:** База даних, що працює в Docker-контейнері  
- **Docker:** Використовується для контейнеризації бази даних  
- **Тести:** Тестування реалізовано за допомогою бібліотеки `pytest`  

---

Цей файл містить:

1. **Короткий опис проекту**  
2. **Інструкції по налаштуванню середовища з використанням `poetry`**  
3. **Інструкції для запуску проекту на Mac та Windows через Docker**  
4. **Інструкції по запуску міграцій та створенню суперкористувача**  
5. **Інструкції для запуску тестів**  
6. **Технічні деталі**  

Ви можете редагувати цей файл відповідно до ваших потреб.