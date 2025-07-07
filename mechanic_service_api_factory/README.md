# 🛠️ Mechanic & Service Ticket API (Factory Pattern)

A beginner-friendly Flask REST API built with the **Application Factory pattern**,
Blue­prints, SQLAlchemy models, Marshmallow schemas, and unit tests.

## 📖 Quick Guide

```bash
# 1. clone + create venv
git clone <repo-url>
cd mechanic_service_api_factory
python -m venv venv
source venv/bin/activate   # windows: venv\Scripts\activate

# 2. install deps
pip install -r requirements.txt

# 3. run the app
flask --app run.py --debug run
# -> http://127.0.0.1:5000
```

## 🔑 Key Concepts for Beginners

| Concept | Where to See It | Why It Matters |
|---------|-----------------|----------------|
| **Application Factory** | `app/__init__.py (create_app)` | Lets you create multiple app instances with different configs (great for tests). |
| **Blueprints** | `blueprints/mechanic`, `blueprints/service_ticket` | Keep resource‑specific code isolated & reusable. |
| **URL Prefixes** | `bp = Blueprint('mechanic', __name__, url_prefix='/mechanics')` | Automatically groups endpoints. |
| **SQLAlchemy Models** | `models.py` | Map Python classes → DB tables. |
| **Many‑to‑Many** | `service_mechanic` table | A ticket can have many mechanics, a mechanic can work many tickets. |
| **Marshmallow Schemas** | `schemas.py` files | (De)serialize JSON without manual field mapping. |
| **Unit Tests** | `tests/` | Confidence that every route works (+ negative cases). |
| **Postman Collection** | `postman_collection.json` | One‑click import to test all endpoints. |

## 🗂️ Folder Structure

```
mechanic_service_api_factory/
├── app/
│   ├── __init__.py         # factory + blueprint register
│   ├── extensions.py       # db and ma instances
│   ├── models.py           # Mechanic, ServiceTicket
│   └── blueprints/
│       ├── mechanic/
│       │   ├── __init__.py
│       │   ├── routes.py
│       │   └── schemas.py
│       └── service_ticket/
│           ├── __init__.py
│           ├── routes.py
│           └── schemas.py
├── tests/
│   ├── test_mechanic.py
│   └── test_service_ticket.py
├── postman_collection.json
├── run.py                  # entrypoint
└── requirements.txt
```

## ✅ Tests

Run **all** tests:

```bash
python -m unittest discover tests
```

Inside each test we:
* create a fresh app with `create_app('testing')`
* use Flask’s `test_client()`
* cover **positive** + **negative** paths for every endpoint.

---

Happy hacking – tweak, extend, and make it your own!
