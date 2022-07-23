#!/usr/bin/env bash
set -e

# Enable Hooks
pre-commit autoupdate
pre-commit install
