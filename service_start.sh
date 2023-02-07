#! /usr/bin/env sh
set -e

echo "# ======================= [1/2] Waiting for Postgres"
until curl http://$POSTGRES_HOST:$POSTGRES_PORT/ 2>&1 | grep '52' && echo "# ======================= Success!" ; do
  >&2 echo "# ======================= Waiting for Postgres to connect..."
  sleep 2
done

echo "# ======================= [2/2] Starting Server"
exec gunicorn -k uvicorn.workers.UvicornWorker -w 4 -b 0.0.0.0:8000 "app.main:app"