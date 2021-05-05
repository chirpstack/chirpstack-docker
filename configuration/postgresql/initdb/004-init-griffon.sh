#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    create role griffon with login password 'griffon';
    create database griffon with owner griffon;
EOSQL
