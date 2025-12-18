# 📝 Blog RESTful API
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Flask-Backend-black?style=for-the-badge&logo=flask">
  <img src="https://img.shields.io/badge/SQLite-Database-blue?style=for-the-badge&logo=sqlite">
  <img src="https://img.shields.io/badge/SQLModel-ORM-green?style=for-the-badge">
</p>
<p align="center">
  <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdHppOGZ0Y2dqb2k5bW5pZ2RuMG82MzQ3bXVuZ3duOWF1aDF3bnU5aCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/C2GtNxNdOfprXhUJGR/giphy.gif" alt="gif" height="505" width="300"/>
</p>
A simple **RESTful Blogging API** built using **Flask**, **SQLModel**, and **SQLite**.  
Supports full CRUD operations, search functionality, and clean request validation.

> Built for learning real backend fundamentals — not tutorial fairy tales.


## 🚀 Features

- Create, Read, Update, Delete blog posts
- Filter posts using a search term
- SQLite database (zero setup)
- Schema-based request validation
- Clean RESTful routes
- No authentication / pagination (intentionally)


## 🛠️ Tech Stack

- **Programming Language**
  - Python 3.10+

- **Backend Framework**
  - Flask — RESTful API development

- **ORM / Data Modeling**
  - SQLModel — ORM + data validation
  - SQLAlchemy — database abstraction (under the hood)
  - Pydantic v2 — schema validation

- **Database**
  - SQLite — lightweight, file-based database

- **API Design**
  - RESTful architecture
  - JSON-based request & response handling
  - Proper HTTP status codes

- **Testing & API Client**
  - Bruno — API testing and debugging

- **Development Tools**
  - Git — version control
  - VS Code — development environment


## 📁 Project Structure
```
Blog RESTful API/
├── main.py # Flask routes
├── database/
│ └── db.py  # Database engine & session
├── models/
│ └── models.py # SQLModel DB models
├── schemas.py # Request validation schemas
├── blog.db # SQLite database (auto-created)
├── requirements.txt
└── README.md
```
## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Average-Chief/RESTful-Blog-API.git
cd RESTful-Blog-API
```

Install dependencies:
```
pip install -r requirements.txt
```

Run the server:
```
flask --app main run
```

Server will start at:
```
http://127.0.0.1:5000
```

## 📌 API Endpoints

### ➕ Create Blog Post
```
POST /posts
```
```
{
  "title": "My First Blog Post",
  "content": "This is my first blog.",
  "category": "Technology",
  "tags": ["Python", "API"]
}
```
Response: ```201 Created```

### 📖 Get All Blog Posts
```
GET /posts
```
Optional search:
```
GET /posts?term=tech
```

### 📄 Get Single Blog Post
```
GET /posts/{id}
```

### 🔄 Update Blog Post
```
PUT /posts/{id}
```
```
{
  "title": "Updated Title",
  "content": "Updated content",
  "category": "Technology",
  "tags": ["Flask"]
}
```
### ❌ Delete Blog Post
```
DELETE /posts/{id}
```
Response: ```204 No Content```

### 🔍 Search Functionality
You can filter blog posts using a wildcard search on:

- title
- content
- category

Example:
```
GET /posts?term=python
```
## 🧠 Design Decisions

- SQLModel used for ORM + validation
- Schemas separate user input from DB models
- SQLite chosen for simplicity and portability
- Bulk operations intentionally excluded (can be added later)

## 🧑‍💻 Author

Built by Average-Chief
Backend learner. Debug survivor. REST enjoyer.

## 📜 License

This project is licensed under the MIT License.

Project: https://roadmap.sh/projects/blogging-platform-api