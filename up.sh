#!/bin/bash

export $(grep -v '^#' .env | xargs -d '\n')

function writers() {
    docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build -d --force-recreate --no-deps balanced-general-writer
}

function readers() {
    docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build -d --force-recreate --no-deps reader-1 reader-2
}

function nginx() {
    docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build -d --force-recreate --no-deps nginx
}

function db() {
    docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build -d --force-recreate --no-deps balanced-reader-db
}

function all() {
    docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build -d --force-recreate
}

if [[ -z "$1" ]]; then
    all
else
    $1
fi