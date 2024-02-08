#!/bin/fish
set -lx PIPENV_PIPFILE /home/rodrigokimura/dev/project_erp/Pipfile
set DEBUG 0
cd /home/rodrigokimura/dev/project_erp/ || exit
pipenv run gunicorn project_erp.wsgi:application \
    --pythonpath src \
    --workers 5 \
    -b 0.0.0.0:8888 \
    --log-level INFO \
    --enable-stdio-inheritance \
    --capture-output \
    -t 30
