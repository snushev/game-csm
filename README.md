# 🎮 GameCMS – Game Backend API

**GameCMS** is a modular, scalable Django REST Framework API for managing players, items, guilds, and quests in an RPG-style game.  
It uses JWT authentication, role-based permissions, PostgreSQL, and auto-documented endpoints with Swagger.

---

## 🚀 Technologies

- Python 3.12+
- Django 5.2+
- Django REST Framework
- Simple JWT (JSON Web Tokens)
- drf-spectacular (Swagger / OpenAPI)
- PostgreSQL
- Docker & Docker-compose

---

## 📘 DRF Elements

- `Pagination` - Shows 10 items on a page.
- `Permissions` - IsAdminOrReadOnly, IsOwner, AllowAny, etc.
- `Search Filter` - Search item by any value.
- `Order Filter` - Order items by any value
- `Throttle` - Limit to 10 or 1000 requests per day for anonymous or auth user respectively.

---

## 🗂️ Project Structure

### 🧑 `players`

- `Player`: profile connected to Django `User`
- `Guild`: player grouping with leader/member roles
- `Report`: players can report each other

### 🧱 `items`

- `Item`: game objects with rarity and price
- `InventoryItem`: ownership and equipment state
- `Transaction`: player-to-player item trades

### 📜 `quests`

- `Quest`: missions with rewards and level requirements
- `QuestProgress`: player quest tracking

### 📣 `core`

- `NewPost`: admin-published news or announcements

---

## 🔐 Authentication

Authentication is handled with **JWT** using `SimpleJWT`:

- `POST /api/token/`: obtain access + refresh tokens
- `POST /api/token/refresh/`: refresh expired access token

Permissions:

- `IsOwnerOrAdminOrReadOnly`: owners or admins have full access
- `is_staff=True` users (admins) have full write access to all resources
- Others are limited to safe (read-only) methods

---

## 📘 API Documentation

Auto-generated via `drf-spectacular`:

- `/api/schema/` – OpenAPI schema
- `/api/schema/swagger-ui/` – Swagger UI

---

## 🧪 Next Steps

- ✅ Add Pytest for testing
- ✅ Add CI/CD (GitHub Actions)

---

## ⚙️ Setup Instructions (PostgreSQL)

### 🔧 Requirements

- Python 3.12+
- PostgreSQL server running (locally or Docker)

### 1. Create `.env` file (optional)

Example contents:

```env
DB_NAME=gamecms
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

### 2. Install dependencies

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Update `settings.py` for PostgreSQL

In `DATABASES` section:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DB_NAME", "gamecms"),
        'USER': os.getenv("DB_USER", "postgres"),
        'PASSWORD': os.getenv("DB_PASSWORD", ""),
        'HOST': os.getenv("DB_HOST", "localhost"),
        'PORT': os.getenv("DB_PORT", "5432"),
    }
}
```

### 4. Apply migrations & run server

```bash
python manage.py migrate
python manage.py runserver
```

## 🧠 Author

Created by SNushev as a backend-only RPG game management API.
Feel free to fork, expand, dockerize, and deploy in your own stack.
