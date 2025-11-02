#!/bin/sh

# Wait for DB
echo "Waiting for database at $DATABASE_HOST:$DATABASE_PORT..."
until nc -z "$DATABASE_HOST" "$DATABASE_PORT"; do
  echo "Database not ready yet..."
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
