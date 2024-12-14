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

#### Get all events

```http
  GET /api-app/all-events/
```

#### Get a specific event

```http
  GET /api-app/get-event/<pk>/
```

| Parameter | Description                |
| :-------- | :------------------------- |
| `pk` | **Required**. Id of item to fetch |





#### Get all news

```http
  GET /api-app/all-news/
```

#### Get a specific event

```http
  GET /api-app/get-new/<pk>/
```

| Parameter | Description                |
| :-------- | :------------------------- |
| `pk` | **Required**. Id of item to fetch |




#### Get all users

```http
  GET /api-auth/all-users/
```

