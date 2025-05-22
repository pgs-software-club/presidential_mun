#!/bin/sh

flask db init
flask db migrate -m "Intial Migration"
flask db upgrade
exec gunicorn -w 4 -b 0.0.0.0:8000 server:app