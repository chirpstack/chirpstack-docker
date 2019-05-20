# LoRa Server Docker setup

This repository contains a skeleton to setup the [LoRa Server](https://www.loraserver.io)
project using [docker-compose](https://docs.docker.com/compose/).

**Note:** Please use this `docker-compose.yml` file as a starting point for testing
but keep in mind that for production usage it might need modifications. 

## Directory layout

* `docker-compose.yml`: the docker-compose file containing the services
* `docker-compose-env.yml`: alternate docker-compose file using environment variables, can be run with the docker-compose `-f` flag
* `configuration/lora*`: directory containing the LoRa Server configuration files, see:
    * https://www.loraserver.io/lora-gateway-bridge/install/config/
    * https://www.loraserver.io/loraserver/install/config/
    * https://www.loraserver.io/lora-app-server/install/config/
    * https://www.loraserver.io/lora-geo-server/install/config/
* `configuration/postgresql/initdb/`: directory containing PostgreSQL initialization scripts

## Configuration

The LoRa Server components are pre-configured to work with the provided
`docker-compose.yml` file and defaults to the EU868 LoRaWAN band. Please refer
to the `configuration/loraserver/examples` directory for more configuration
examples.

# Data persistence

PostgreSQL and Redis data is persisted in Docker volumes, see the `docker-compose.yml`
`volumes` definition.

## Requirements

Before using this `docker-compose.yml` file, make sure you have [Docker](https://www.docker.com/community-edition)
installed.

## Usage

To start all the LoRa Server components, simply run:

```bash
$ docker-compose up
```

**Note:** during the startup of services, it is normal to see the following errors:

* ping database error, will retry in 2s: dial tcp 172.20.0.4:5432: connect: connection refused
* ping database error, will retry in 2s: pq: the database system is starting up


After all the components have been initialized and started, you should be able
to open http://localhost:8080/ in your browser.

### Add network-server

When adding the network-server in the LoRa App Server web-interface
(see [network-servers](https://www.loraserver.io/lora-app-server/use/network-servers/)),
you must enter `loraserver:8000` as the network-server `hostname:IP`.
