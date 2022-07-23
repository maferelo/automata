#!/bin/sh

# Let the DB start
sleep 10;
# Run migrations
alembic upgrade head

# Hand off to the CMD
exec "$@"
