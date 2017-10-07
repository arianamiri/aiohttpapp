#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE USER concierge_app;
    ALTER USER concierge_app WITH PASSWORD 'password';
    CREATE DATABASE concierge;
    GRANT ALL PRIVILEGES ON DATABASE concierge TO concierge_app;
EOSQL
