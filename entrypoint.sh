#!/bin/sh

echo "Waiting for MariaDB to be ready..."
while ! nc -z "$DATABASE_HOST" "$DATABASE_PORT"; do
  sleep 1
done

# Run migrations
echo "Running migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
yes | python manage.py collectstatic --clear --noinput

# Start the application
exec "$@"
