## Django Project Setup Guide


### 1. Clone the Repository

```bash
git clone https://github.com/ordenmeny/unit_site.git
cd unit_site
```

### 2. Set Up a Virtual Environment
```bash 
python -m venv venv
```
Windows:
```bash
venv\Scripts\activate
```


macOS/Linux:
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r req.txt
```

### 4. Configure the Database
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 5. Start the Development Server
```bash
python manage.py runserver
```

The project will be accessible at:
http://127.0.0.1:8000/

---


## API Reference

### Events:
#### 1) Get all events

```http
  GET /api-app/all-events/
```
#### Response
```json
[
  {
    "id": 1,
    "name": "Встреча 1",
    "date": "YYYY-MM-DD",
    "time": "HH:MM:SS",
    "place": "В ИРИТ-РТФ",
    "description": "Питчинг проектов"
  }
]
```


#### 2) Get a specific event

```http
  GET /api-app/get-event/<pk>/
```

| Parameter | Description                |
| :-------- | :------------------------- |
| `pk` | **Required**. Id of item to fetch |


---

### News:
#### 1) Get all news

```http
  GET /api-app/all-news/
```

#### Response
```json

[
  {
    "id": 1,
    "title": "Новость 1",
    "text": "Текст к новости 1",
    "date_created": "YYYY-MM-DD"
  }
]
```

#### 2) Get a specific news

```http
  GET /api-app/get-new/<pk>/
```

| Parameter | Description                |
| :-------- | :------------------------- |
| `pk` | **Required**. Id of item to fetch |


---

### Users:
#### 1) Get all users

```http
  GET /api-auth/all-users/
```

#### Response
```json
[
    {
        "id": 6,
        "first_name": "Иван",
        "last_name": "Коваленко",
        "social_link": "lenin.com",
        "description": "Описание",
        "position": "Дезигнер"
    }
]
```


#### 2) Get a specific user by id
```http
  GET /api-auth/get-user/<id>/
```


#### Response
```json
{
        "id": 7,
        "first_name": "Иван 2",
        "last_name": "Коваленко 2",
        "social_link": "lenin.com 2",
        "description": "Описание 2",
        "position": "Дезигнер 2"
}
```

---

### Projects:
#### 1) Get all projects

```http
  GET /api-auth/all-projects/
```

#### Response
```json
[
    {
        "id": 1,
        "name": "NewsMobile",
        "description": "Описание проекта",
        "link": "https://newsmobile.com/"
    }
]
```


#### 2) Get a specific project by id
```http
  GET /api-auth/get-project/<id>/
```


#### Response
```json
{
    "id": 1,
    "name": "NewsMobile",
    "description": "Описание проекта",
    "link": "https://newsmobile.com/"
}
```

