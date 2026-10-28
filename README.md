# FastAPI CRUD Tutorial

Backend API sederhana menggunakan FastAPI dan SQLite untuk mengelola users dan posts.

## Tech Stack

- **FastAPI** - Modern Python web framework
- **SQLite** - Lightweight database
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server

## Features

- CRUD operations untuk users dan posts
- Data validation otomatis
- Interactive API documentation (Swagger UI)
- RESTful API design
- Relational database (foreign key)

## Installation

```bash
pip install fastapi uvicorn
```

## Database Setup

Database akan otomatis terbuat saat pertama kali run. Struktur table:

**Users:**
- id (PRIMARY KEY)
- username
- email
- age

**Posts:**
- id (PRIMARY KEY)
- user_id (FOREIGN KEY)
- title
- content

## Running the Server

```bash
uvicorn main:app --reload
```

Server akan berjalan di `http://localhost:8000`

## API Documentation

Buka browser ke `http://localhost:8000/docs` untuk interactive API documentation.

## API Endpoints

### Users

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /users | Get all users |
| GET | /users/{id} | Get user by ID |
| POST | /users | Create new user |
| PUT | /users/{id} | Update user |
| DELETE | /users/{id} | Delete user |

### Posts

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /posts | Get all posts |
| POST | /posts | Create new post |

## Example Usage

**Create User:**
```json
POST /users
{
  "username": "budi",
  "email": "budi@mail.com",
  "age": 25
}
```

**Create Post:**
```json
POST /posts
{
  "user_id": 1,
  "title": "My First Post",
  "content": "Hello World!"
}
```

## Learning Journey

Project ini dibuat sebagai bagian dari pembelajaran backend Python dengan fokus:
- RESTful API design
- Database relational
- HTTP methods & status codes
- Data validation

## Next Steps

- [ ] Authentication (JWT)
- [ ] Password hashing
- [ ] Pagination
- [ ] PostgreSQL migration
- [ ] Docker deployment

## License

MIT
