#!/bin/bash
set -e

# PostgreSQL commands to create a new role and database for ChirpStack
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    create role chirpstack with login password 'chirpstack';
    create database chirpstack_integration with owner chirpstack;
EOSQL
