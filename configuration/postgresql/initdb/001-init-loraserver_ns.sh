#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    create role loraserver_ns with login password 'loraserver_ns';
    create database loraserver_ns with owner loraserver_ns;
EOSQL
