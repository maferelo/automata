#!/usr/bin/env sh
set -e

# Run migrations
alembic upgrade head
