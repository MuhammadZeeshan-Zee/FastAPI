# FastAPI Beginner Setup Guide (Using pip + venv)

This guide explains:

- Python package manager
- Virtual environments (venv)
- Installing packages
- Activating environments
- Starting FastAPI project
- Pydantic schemas
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

# 7. Create First FastAPI App

Create file:

```txt
main.py
```

Add:

```python
from fastapi import FastAPI
from pydantic import BaseModel

# User Schema
class User(BaseModel):
    name: str
    age: int

# Vehicle Schema
class Vehicle(BaseModel):
    model: str
    company: str

app = FastAPI()

@app.get("/")
def home():
    return {"message": "welcome to home page"}

@app.get("/users")
def get_users():
    users = ["ali", "abdullah"]
    return users

@app.post("/users")
def create_user(user: User):
    return user

@app.post("/vehicles")
def create_vehicle(vehicle: Vehicle):
    return vehicle
```

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

These classes:

```python
class User(BaseModel):
```

and

```python
class Vehicle(BaseModel):
```

are called:

```txt
Schemas
```

Schemas define:

- request structure
- response structure
- validation rules

---

# Why Are Schemas Important?

Without schemas:

- data becomes messy
- validation becomes manual
- APIs become unreliable

Schemas make APIs:

- clean
- validated
- predictable
- production-ready

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

Example response:

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

# Understanding the Routes

| Method | Route | Purpose |
|------|------|------|
| GET | / | Home route |
| GET | /users | Get users |
| POST | /users | Create user |
| POST | /vehicles | Create vehicle |

---

# GET Route Example

```python
@app.get("/users")
def get_users():
    users = ["ali", "abdullah"]
    return users
```

Purpose:

```txt
Retrieve data
```

---

# POST Route Example

```python
@app.post("/users")
def create_user(user: User):
    return user
```

Purpose:

```txt
Create data
```

---

# Request Body Example

## POST /users

### Request

```json
{
  "name": "Ali",
  "age": 22
}
```

### Response

```json
{
  "name": "Ali",
  "age": 22
}
```

---

# Vehicle Request Example

## POST /vehicles

### Request

```json
{
  "model": "Civic",
  "company": "Honda"
}
```

### Response

```json
{
  "model": "Civic",
  "company": "Honda"
}
```

---

# Query Parameters vs Request Body

## Query Parameters

Example:

```txt
/products?page=1
```

Used mostly for:

- filtering
- searching
- sorting
- pagination

---

## Request Body

Used for:

- creating resources
- sending structured data
- large payloads

Example:

```json
{
  "name": "Ali",
  "age": 22
}
```

---

# Important FastAPI Rule

## Primitive Types → Query Parameters

Example:

```python
def get_user(name: str):
```

FastAPI treats this as:

```txt
Query parameter
```

---

## Pydantic Models → Request Body

Example:

```python
def create_user(user: User):
```

FastAPI treats this as:

```txt
JSON request body
```

---

# Why Using Schemas is Better

Bad:

```python
def create_vehicle(model: str, company: str):
```

Better:

```python
def create_vehicle(vehicle: Vehicle):
```

Why?

Because schemas provide:

- validation
- scalability
- cleaner APIs
- reusable structures
- automatic documentation

This is how production APIs are built.

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

This is one reason FastAPI became extremely popular.

---

# Test the Routes

## Home Route

### Request

```txt
GET /
```

### Response

```json
{
  "message": "welcome to home page"
}
```

---

# Get Users Route

### Request

```txt
GET /users
```

### Response

```json
[
  "ali",
  "abdullah"
]
```

---

# Create User Route

### Request

```txt
POST /users
```

### Request Body

```json
{
  "name": "Ali",
  "age": 22
}
```

### Response

```json
{
  "name": "Ali",
  "age": 22
}
```

---

# Create Vehicle Route

### Request

```txt
POST /vehicles
```

### Request Body

```json
{
  "model": "Civic",
  "company": "Honda"
}
```

### Response

```json
{
  "model": "Civic",
  "company": "Honda"
}
```

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

Using primitive types for complex request data.

Bad:

```python
def create_vehicle(model: str, company: str):
```

Better:

```python
def create_vehicle(vehicle: Vehicle):
```

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
venv + pip + requirements.txt + Pydantic
```

first is extremely important because these are core Python backend fundamentals.