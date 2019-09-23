#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    create role loraserver_ns with login password '$POSTGRES_PASSWORD';
    create database loraserver_ns with owner loraserver_ns;
EOSQL
