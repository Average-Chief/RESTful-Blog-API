# 📝 Blog RESTful API

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Backend-black?style=for-the-badge&logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?style=for-the-badge&logo=sqlite)
![SQLModel](https://img.shields.io/badge/SQLModel-ORM-green?style=for-the-badge)

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
git clone https://github.com/yourusername/blog-rest-api.git
cd blog-rest-api
```
