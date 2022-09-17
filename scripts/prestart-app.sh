#!/usr/bin/env sh
# Stop if error
set -e

# Apply migrations
alembic upgrade head
