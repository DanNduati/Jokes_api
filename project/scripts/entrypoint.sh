#!/bin/sh
echo "Waiting for postgress..."

while ! nc -z web-db 5432; do
    sleep 0.1
done

echo "PostgreSQL started!"
exec "$@" #takes any command line arguments passed to entrypoint.sh and execs them as a command