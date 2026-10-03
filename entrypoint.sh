#!/bin/sh
set -e

mkdir -p /app/data /app/media

# Seed the persistent database volume from the db.sqlite3 shipped in the image.
if [ ! -f /app/data/db.sqlite3 ] && [ -f /app/db.sqlite3 ]; then
    echo "Seeding /app/data/db.sqlite3 from image copy"
    cp /app/db.sqlite3 /app/data/db.sqlite3
fi

chown -R app:app /app/data /app/media

python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec gosu app gunicorn blogkarla.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --timeout 60 \
    --access-logfile -