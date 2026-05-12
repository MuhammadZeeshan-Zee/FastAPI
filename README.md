# FastAPI Beginner Setup Guide (Using pip + venv)

This guide explains:

- Python package manager
- Virtual environments (venv)
- Installing packages
- Activating environments
- Starting FastAPI project
- CRUD APIs
- Pydantic schemas
- Path parameters
- Request validation
- requirements.txt
- Industry best practices
- Common beginner mistakes

---

# 1. What is a Package Manager in Python?

A package manager helps us:

- install libraries
- update libraries
- remove libraries
- manage dependencies

Example packages:

- fastapi
- uvicorn
- sqlalchemy
- pydantic

---

# Which Package Manager Are We Using?

We are using:

```txt
pip
```

---

# What is pip?

`pip` is Python’s default package manager.

It comes with Python.

We use it to install packages from:

```txt
PyPI (Python Package Index)
```

Think of PyPI like:

```txt
Python App Store
```

---

# Example

Install FastAPI:

```bash
pip install fastapi
```

Install Uvicorn:

```bash
pip install uvicorn
```

---

# 2. What is venv (Virtual Environment)?

A virtual environment is an isolated Python environment.

It creates a separate space for project dependencies.

---

# Why Do We Need venv?

Without venv:

```txt
All projects share same packages
```

This creates problems:

- version conflicts
- broken projects
- messy global Python environment

---

# Example Problem

Project A needs:

```txt
FastAPI 0.95
```

Project B needs:

```txt
FastAPI 0.115
```

Without venv → conflicts happen.

---

# With venv

Each project gets:

- separate packages
- isolated dependencies
- clean environment

This is industry standard.

---

# 3. Create Project Folder

```bash
mkdir fastapi-learning

cd fastapi-learning
```

---

# 4. Create Virtual Environment

## Command

```bash
python -m venv venv
```

OR

```bash
py -m venv venv
```

---

# Command Breakdown

```txt
python -m venv venv
```

| Part | Meaning |
|------|----------|
| python | Run Python |
| -m | Run module |
| venv | Virtual environment module |
| venv | Folder name |

---

# What Happens Internally?

Python creates:

```txt
venv/
```

folder containing:

- isolated Python interpreter
- isolated pip
- project packages

---

# 5. Activate Virtual Environment

## Windows CMD

```bash
venv\Scripts\activate
```

---

## Windows PowerShell

```bash
.\venv\Scripts\Activate.ps1
```

---

## Mac/Linux

```bash
source venv/bin/activate
```

---

# How to Know venv is Activated?

You will see:

```txt
(venv)
```

Example:

```txt
(venv) C:\fastapi-learning>
```

---

# VERY IMPORTANT

Always activate venv BEFORE:

- installing packages
- running pip freeze
- running FastAPI

---

# Why?

Because:

```txt
pip works against the CURRENT active Python environment
```

---

# 6. Install FastAPI and Uvicorn

## Command

```bash
pip install fastapi uvicorn
```

---

# What Are These Packages?

| Package | Purpose |
|----------|----------|
| fastapi | API framework |
| uvicorn | ASGI server |

---

# What is Uvicorn?

FastAPI itself does not run servers.

Uvicorn is the server that runs FastAPI applications.

Think:

```txt
FastAPI = Car Engine
Uvicorn = Driver
```

---

# 7. Create First FastAPI CRUD App

Create file:

```txt
main.py
```

Add:

```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

class User(BaseModel):
    name: str
    age: int

app = FastAPI()

users: List[User] = []

@app.get("/")
def home():
    return {"message": "welcome to home page"}

@app.get("/user")
def get_all_user():
    return users

@app.post("/user")
def create_user(user: User):
    users.append(user)
    return {"message": "user created successfully"}

@app.get("/user/{id}")
def get_user(id: int):
    return users[id]

@app.put("/user/{id}")
def update_user(id: int, user: User):
    users[id] = user
    return user

@app.delete("/user/{id}")
def delete_user(id: int):
    users.pop(id)
    return users
```

---

# What is CRUD?

CRUD stands for:

| Operation | Meaning |
|------|------|
| Create | Add data |
| Read | Fetch data |
| Update | Modify data |
| Delete | Remove data |

---

# Our CRUD Routes

| Method | Route | Purpose |
|------|------|------|
| GET | / | Home route |
| GET | /user | Get all users |
| POST | /user | Create user |
| GET | /user/{id} | Get single user |
| PUT | /user/{id} | Update user |
| DELETE | /user/{id} | Delete user |

---

# What is BaseModel?

```python
from pydantic import BaseModel
```

`BaseModel` comes from Pydantic.

Pydantic is used for:

- data validation
- request parsing
- type checking
- automatic serialization

FastAPI heavily depends on Pydantic.

---

# What Are Schemas?

This class:

```python
class User(BaseModel):
```

is called a:

```txt
Schema
```

Schemas define:

- request structure
- response structure
- validation rules

---

# User Schema Example

```python
class User(BaseModel):
    name: str
    age: int
```

This means:

| Field | Type |
|------|------|
| name | string |
| age | integer |

---

# What Happens Internally?

When request comes:

```json
{
  "name": "Ali",
  "age": 22
}
```

FastAPI + Pydantic:

1. read JSON body
2. validate fields
3. validate types
4. convert into Python object
5. pass to function

Automatically.

---

# What if Invalid Data Comes?

Example:

```json
{
  "name": "Ali",
  "age": "hello"
}
```

FastAPI automatically returns validation error.

Example:

```json
{
  "detail": [
    {
      "type": "int_parsing",
      "loc": ["body", "age"],
      "msg": "Input should be a valid integer"
    }
  ]
}
```

---

# What is List[User]?

```python
users: List[User] = []
```

This means:

```txt
users will store a list of User objects
```

---

# Why Use Type Hinting?

Type hints improve:

- readability
- autocomplete
- debugging
- scalability
- developer experience

This is industry standard.

---

# Understanding CRUD Routes

# Create User

```python
@app.post("/user")
def create_user(user: User):
    users.append(user)
    return {"message": "user created successfully"}
```

Purpose:

```txt
Add new user
```

---

# Get All Users

```python
@app.get("/user")
def get_all_user():
    return users
```

Purpose:

```txt
Retrieve all users
```

---

# Get Single User

```python
@app.get("/user/{id}")
def get_user(id: int):
    return users[id]
```

Purpose:

```txt
Retrieve single user
```

---

# Update User

```python
@app.put("/user/{id}")
def update_user(id: int, user: User):
    users[id] = user
    return user
```

Purpose:

```txt
Update existing user
```

---

# Delete User

```python
@app.delete("/user/{id}")
def delete_user(id: int):
    users.pop(id)
    return users
```

Purpose:

```txt
Delete user
```

---

# What is a Path Parameter?

Example:

```python
@app.get("/user/{id}")
```

Here:

```txt
{id}
```

is called a:

```txt
Path Parameter
```

---

# Example Request

```txt
GET /user/0
```

FastAPI extracts:

```python
id = 0
```

automatically.

---

# Query Parameters vs Path Parameters

## Path Parameter

Used for identifying resources.

Example:

```txt
/user/1
```

---

## Query Parameter

Used for filtering/searching.

Example:

```txt
/users?page=1
```

---

# Swagger Docs

Open:

```txt
http://127.0.0.1:8000/docs
```

---

# Why Swagger Docs Are Amazing

FastAPI automatically generates:

- API documentation
- request body forms
- schema validation
- interactive testing UI

---

# Example Requests

# Create User

## Request

```txt
POST /user
```

## Body

```json
{
  "name": "Ali",
  "age": 22
}
```

## Response

```json
{
  "message": "user created successfully"
}
```

---

# Get All Users

## Request

```txt
GET /user
```

## Response

```json
[
  {
    "name": "Ali",
    "age": 22
  }
]
```

---

# Get Single User

## Request

```txt
GET /user/0
```

## Response

```json
{
  "name": "Ali",
  "age": 22
}
```

---

# Update User

## Request

```txt
PUT /user/0
```

## Body

```json
{
  "name": "Abdullah",
  "age": 25
}
```

## Response

```json
{
  "name": "Abdullah",
  "age": 25
}
```

---

# Delete User

## Request

```txt
DELETE /user/0
```

## Response

```json
[]
```

---

# Important Beginner Learning

Current data storage:

```python
users = []
```

is:

- temporary
- in-memory
- not persistent

After server restart:

```txt
All data disappears
```

---

# Why This is NOT Production Ready

Problems:

- data loss
- no persistence
- no scalability
- no concurrency safety

---

# Real Production Systems Use

- PostgreSQL
- MongoDB
- MySQL
- Redis

Later we will learn:

- SQLAlchemy
- Prisma
- Async database handling
- Repository pattern

---

# 8. Run FastAPI Server

## Command

```bash
uvicorn main:app --reload
```

---

# Command Breakdown

| Part | Meaning |
|------|----------|
| uvicorn | Run ASGI server |
| main | File name |
| app | FastAPI instance |
| --reload | Auto restart on file changes |

---

# Open in Browser

Swagger Docs:

```txt
http://127.0.0.1:8000/docs
```

---

# Alternative Docs

```txt
http://127.0.0.1:8000/redoc
```

---

# 9. Install More Packages

Examples:

```bash
pip install sqlalchemy
```

```bash
pip install pymongo
```

```bash
pip install python-jose
```

---

# 10. Where Are Packages Stored?

Packages are installed inside:

```txt
venv/
```

That is why environments stay isolated.

---

# 11. What is requirements.txt?

It stores project dependencies.

Example:

```txt
fastapi==0.115.0
uvicorn==0.30.0
sqlalchemy==2.0.0
```

---

# Why Use requirements.txt?

It helps:

- other developers
- deployment servers
- production systems

install exact dependencies.

---

# 12. Create requirements.txt

## IMPORTANT

Make sure venv is ACTIVATED first.

Then run:

```bash
pip freeze > requirements.txt
```

---

# What Does pip freeze Do?

It exports installed packages and versions.

Example:

```txt
fastapi==0.115.0
uvicorn==0.30.0
```

---

# VERY IMPORTANT CONCEPT

If venv is NOT activated:

```txt
pip freeze may export global packages
```

This is a common beginner mistake.

---

# Correct Workflow

✅ Activate venv first

THEN:

```bash
pip freeze > requirements.txt
```

---

# 13. Install Packages from requirements.txt

## First Activate venv

Then run:

```bash
pip install -r requirements.txt
```

---

# What Happens Here?

| Part | Meaning |
|------|----------|
| pip install | Install packages |
| -r | Read from file |
| requirements.txt | Dependency file |

---

# 14. Recommended Beginner Project Structure

```txt
project/
│
├── venv/
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 15. Create .gitignore

Create file:

```txt
.gitignore
```

Add:

```txt
venv/
__pycache__/
```

---

# Why Ignore venv?

Because:

- huge size
- OS-specific files
- unnecessary for GitHub

---

# 16. Common Beginner Mistakes

## Mistake 1

Installing packages WITHOUT activating venv.

Problem:

```txt
Packages install globally
```

---

## Mistake 2

Running pip freeze outside venv.

Problem:

```txt
requirements.txt becomes polluted
```

---

## Mistake 3

Using list index as database ID.

Example:

```python
users[id]
```

Problem:

- unstable IDs
- index errors
- not production-safe

Later we will use real database IDs.

---

## Mistake 4

Uploading venv to GitHub.

Problem:

```txt
Huge repository size
```

---

# 17. Best Practices

## Always:

✅ Create venv  
✅ Activate venv  
✅ Install packages inside venv  
✅ Use Pydantic schemas  
✅ Use type hints  
✅ Freeze dependencies  
✅ Use requirements.txt  

---

# 18. Final Beginner Workflow

## Step 1 — Create Project

```bash
mkdir fastapi-learning

cd fastapi-learning
```

---

## Step 2 — Create venv

```bash
python -m venv venv
```

---

## Step 3 — Activate venv

### Windows

```bash
venv\Scripts\activate
```

---

## Step 4 — Install Packages

```bash
pip install fastapi uvicorn
```

---

## Step 5 — Create requirements.txt

```bash
pip freeze > requirements.txt
```

---

## Step 6 — Run FastAPI

```bash
uvicorn main:app --reload
```

---

# 19. Industry Note

Modern backend systems heavily rely on:

- request validation
- typed schemas
- API contracts
- automatic documentation

FastAPI + Pydantic make backend development:

- fast
- scalable
- clean
- developer-friendly

Learning:

```txt
venv + pip + Pydantic + CRUD APIs
```

first is extremely important because these are core Python backend fundamentals.