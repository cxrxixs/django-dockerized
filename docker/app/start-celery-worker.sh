#!/bin/sh
celery -A app worker -Q $1 -l info
