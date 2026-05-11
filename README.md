# FastAPI Beginner Setup Guide (Using pip + venv)

This guide explains:

- Python package manager
- Virtual environments (venv)
- Installing packages
- Activating environments
- Starting FastAPI project
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

app = FastAPI()

@app.get("/")
def home():
    return {"message": "welcome to home page"}

@app.get("/users")
def get_users():
    users = ["ali", "abdullah"]
    return users

@app.post("/users")
def create_user():
    return {"message": "user added"}
```

---

# Understanding the Routes

| Method | Route | Purpose |
|------|------|------|
| GET | / | Home route |
| GET | /users | Get all users |
| POST | /users | Create user |

---

# What is @app.get()?

```python
@app.get("/")
```

This tells FastAPI:

```txt
When someone sends a GET request to "/",
run this function.
```

---

# What is @app.post()?

```python
@app.post("/users")
```

This tells FastAPI:

```txt
When someone sends a POST request to "/users",
run this function.
```

---

# What is an API Route?

Routes are endpoints users or frontend applications access.

Example:

```txt
GET /users
```

means:

```txt
Fetch users data
```

---

# Difference Between GET and POST

| Method | Purpose |
|------|------|
| GET | Retrieve data |
| POST | Create data |
| PUT | Update data |
| DELETE | Remove data |

---

# 8. Run FastAPI Server

## Command

```bash
uvicorn main:app --reload
```

---

# Open Swagger UI

```txt
http://127.0.0.1:8000/docs
```

---

# Why Swagger Docs Are Amazing

FastAPI automatically generates:

- API documentation
- route testing UI
- request schemas
- response docs

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

### Response

```json
{
  "message": "user added"
}
```

---

# Current Project Structure

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

# Important Beginner Learning

Right now:

```python
users = ["ali", "abdullah"]
```

is temporary in-memory data.

This means:

- data disappears after server restart
- not production-ready
- not scalable

Later we will replace this with:

- PostgreSQL
- MongoDB
- SQLAlchemy
- proper database architecture


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

# 14. Recommended Project Structure

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

Forgetting requirements.txt.

Problem:

```txt
Project fails on another machine
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

Modern companies are gradually moving toward:

- uv
- poetry
- pyproject.toml

But learning:

```txt
venv + pip + requirements.txt
```

first is VERY important.

Because it teaches:

- Python environments
- dependency management
- package isolation
- ecosystem fundamentals

These concepts are used everywhere.
