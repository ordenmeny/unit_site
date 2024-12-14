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