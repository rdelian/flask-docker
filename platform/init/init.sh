#!/usr/bin/env bash
if [ ! -d "/platform/migrations" ]; then
  # Control will enter here if $DIRECTORY doesn't exist.
  flask db init -d /platform/migrations
fi
flask db migrate -m "up" -d /platform/migrations
flask db upgrade -d /platform/migrations

echo "" > /platform/logs/error.log
echo "" > /platform/logs/access.log

if test $FLASK_ENV = 'development'; then
    flask run --host=0.0.0.0 --port=80
else
    /usr/sbin/apache2ctl -D FOREGROUND
fi