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