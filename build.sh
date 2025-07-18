#!/usr/bin/env bash

# خروج اگر خطایی پیش اومد
set -o errexit

# نصب وابستگی‌ها
pip install --upgrade pip
pip install -r requirements.txt

# migrate
python manage.py migrate

# جمع‌آوری استاتیک‌ها
python manage.py collectstatic --noinput

#python manage.py createsu