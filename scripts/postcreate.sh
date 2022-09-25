#!/bin/bash
# Stop if error
set -e

# Apply migrations
alembic upgrade head
