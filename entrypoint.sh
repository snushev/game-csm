#!/bin/sh

echo "📦 Waiting for PostgreSQL to start..."
sleep 5

echo "⚙️ Running migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "👤 Creating superuser (if not exists)..."
echo "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
" | python manage.py shell

echo "🚀 Starting server..."
exec python manage.py runserver 0.0.0.0:8000
