#!/bin/sh

# Wait for DB
echo "Waiting for database..."
while ! nc -z db 3306; do
  sleep 1
done

# Run migrations
echo "Running migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# set up seed data
python manage.py run_seed_data

# Start Django dev server
echo "Starting server..."
python manage.py runserver 0.0.0.0:8000
