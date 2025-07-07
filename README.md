
# Mechanic Service API - Deployment & CI/CD Ready

This project is a Flask-based REST API for managing mechanics and service tickets, structured with the Application Factory pattern. It supports CI/CD using GitHub Actions and is deployable to Render.

---

## 🚀 Features

- CRUD for Mechanics and Service Tickets
- Blueprint-based modular architecture
- PostgreSQL-compatible via SQLAlchemy
- Swagger-ready (UI available)
- CI/CD pipeline using GitHub Actions
- Render-compatible deployment with `gunicorn`

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```
DATABASE_URI=your_postgres_database_uri
SECRET_KEY=your_flask_secret
```

**Important:** `.env` is in `.gitignore` and must be created manually.

---

## ▶️ Running Locally

```bash
flask --app flask_app run
```

---

## 🧪 Running Tests

```bash
python -m unittest discover tests
```

---

## 🚢 Deploying to Render

### 1. Connect GitHub Repo

- Go to [https://render.com](https://render.com)
- Create a new Web Service
- Choose your GitHub repository
- Set the build command: `pip install -r requirements.txt`
- Set the start command: `gunicorn flask_app:app`

### 2. Set Environment Variables on Render

- `DATABASE_URI` → your PostgreSQL Render DB URI
- `SECRET_KEY` → your Flask app secret

---

## 🔁 CI/CD Pipeline with GitHub Actions

- On push or PR to `main`, GitHub Actions:
  - Installs dependencies
  - Runs all tests
  - Deploys to Render if tests pass

### GitHub Secrets Required

In your repo's GitHub → Settings → Secrets and variables → Actions:

- `RENDER_API_KEY` – from your Render account
- `SERVICE_ID` – your Render service ID (e.g. `srv-abc123xyz`)

---

## 📄 Swagger Documentation

- Adjust `host` in Swagger docs to match your deployed domain (no `https://`)
- Update `schemes` to `["https"]`

---

## 🧰 File Structure

```
.
├── app/
│   ├── __init__.py
│   ├── models.py
│   └── blueprints/
├── flask_app.py
├── requirements.txt
├── .env            # NOT committed
├── .gitignore
├── Procfile
├── tests/
└── .github/
    └── workflows/
        └── main.yaml
```

---
