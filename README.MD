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

---

## API for authentication
#### URL Prefix
`api-auth/`


### 1. Authorization

**Endpoint:**  
`POST /auth/token/login/`

**Request Parameters:**  
- `username=<username>`  
- `password=<password>`

**Response:**
```json
{
  "auth_token": "your_generated_token"
}
```

**Description:**  
Retrieve a token. The token should be saved on the client side.

---

### 2. Create a new user

**Endpoint:**  
`POST /auth/users/`

**Request Parameters:**  
- `username=<username>`  
- `password=<password>`
- `email=<email>`

---

### 3. Retrieve All Users 
(for admin only)

**Endpoint:**  
`GET /auth/users/`

**Headers:**  
`Authorization: Token <token>`

---

### 4. Retrieve Current User

**Endpoint:**  
`GET /auth/users/me/`

**Headers:**  
`Authorization: Token <token>`


---

---


## URL for events
#### All urls For authorized users only.
All API endpoints are prefixed with:
```
api-app/
```

## Endpoints

### 1. Create Event (Admin Only)
**URL:**
```
POST create-event/
```

**Description:**
Creates a new event.

**Request Body:**
```json
{
    "name": "string",
    "description": "string",
    "place": "string",
    "date": "YYYY-MM-DD",
    "time": "HH:MM:SS"
}
```

**Response:**
```json
{
    "id": 1,
    "name": "string",
    "description": "string",
    "date": "YYYY-MM-DD",
    "time": "HH:MM:SS",
    "place": "string"
}
```

---

### 2. Get All Events
**URL:**
```
GET all-events/
```

**Description:**
Fetches a list of all events.

**Response:**
```json
[
    {
        "id": 1,
        "name": "string",
        "description": "string",
        "date": "YYYY-MM-DD",
        "time": "HH:MM:SS",
        "place": "string"
    },
    {
        "id": 2,
        "name": "string",
        "description": "string",
        "date": "YYYY-MM-DD",
        "time": "HH:MM:SS",
        "place": "string"
    }
]
```

---

### 3. Get Event by ID
**URL:**
```
GET get-event/<int:pk>/
```

**Description:**
Fetches details of a specific event by its ID. Accessible to all users.

**Path Parameters:**
- `pk` (integer): ID of the event.

**Response:**
```json
{
    "id": 1,
    "name": "string",
    "description": "string",
    "date": "YYYY-MM-DD",
    "time": "HH:MM:SS",
    "place": "string"
}
```


---

### 4. Update/Delete Event (Admin Only)
**URL:**
```
PATCH upd-del-event/<int:pk>/
```

**Description:**
Updates or deletes a specific event.

**Path Parameters:**
- `pk` (integer): ID of the event.

**Request Body (for update, all fields are optional):**
```json
{
    "name": "string",
    "description": "string",
    "date": "YYYY-MM-DD",
    "time": "HH:MM:SS",
    "location": "string"
}
```

**Response:**
```json
{
    "id": 1,
    "name": "updated string",
    "description": "updated string",
    "date": "updated YYYY-MM-DD",
    "time": "updated HH:MM:SS",
    "place": "updated string"
}
```

---