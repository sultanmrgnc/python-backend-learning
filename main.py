from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# Pydantic model untuk validation
class UserCreate(BaseModel):
    username: str
    email: str
    age: int

class User(BaseModel):
    id: int
    username: str
    email: str
    age: int

class PostCreate(BaseModel):
    user_id: int
    title: str
    content: str

# Helper function
def get_db():
    return sqlite3.connect('myapp.db')

# GET semua users
@app.get("/users")
def get_users():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    
    result = []
    for user in users:
        result.append({"id": user[0], "username": user[1], "email": user[2], "age": user[3]})
    return result

# GET user by ID
@app.get("/users/{user_id}")
def get_user(user_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {"id": user[0], "username": user[1], "email": user[2], "age": user[3]}

# GET posts 
@app.get("/posts")
def get_posts():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    conn.close()

    result = []
    for post in posts:
        result.append({"id": post[0], "user_id": post[1], "title": post[2], "content": post[3]})
    return result

# POST create user
@app.post("/users")
def create_user(user: UserCreate):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, email, age) VALUES (?, ?, ?)", (user.username, user.email, user.age))
    conn.commit()
    user_id = cursor.lastrowid
    conn.close()
    
    return {"id": user_id, "username": user.username, "email": user.email, "age": user.age}

# POST posts
@app.post("/posts")
def create_post(post: PostCreate):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO posts (user_id, title, content) VALUES (?, ?, ?)", (post.user_id, post.title, post.content))
    
    conn.commit()
    post_id =cursor.lastrowid
    conn.close()

    return {"id": post_id, "user_id": post.user_id, "title": post.title, "content": post.content}

# PUT update user
@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserCreate):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    if not cursor.fetchone():
        conn.close()
        raise HTTPException(status_code=404, detail="User not found")
    
    cursor.execute("UPDATE users SET username = ?, email = ?, age = ? WHERE id = ?", (user.username, user.email, user.age, user_id))
    conn.commit()
    conn.close()
    
    return {"id": user_id, "username": user.username, "email": user.email, "age": user.age}

# DELETE user
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    if not cursor.fetchone():
        conn.close()
        raise HTTPException(status_code=404, detail="User not found")
    
    cursor.execute("DELETE FROM posts WHERE user_id = ?", (user_id,))
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    
    return {"message": "User deleted"}