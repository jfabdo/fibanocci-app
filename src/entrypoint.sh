#!/bin/sh

gunicorn --bind=0.0.0.0:${FLASK_PORT:-8080} --workers=2 --log-level=info --access-logfile='-' --access-logformat="FIB-API - INFO - GUNICORN - %(m)s %(U)s from %(h)s returned %(s)s in %(L)s sec. X-Forwarded-For header: %({X-Forwarded-For}i)s" wsgi:app
