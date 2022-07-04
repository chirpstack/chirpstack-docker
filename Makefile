import-lorawan-devices:
	rm -rf lorawan-devices
	git clone https://github.com/TheThingsNetwork/lorawan-devices
	docker-compose run --rm chirpstack -c /etc/chirpstack import-ttn-lorawan-devices -d /opt/lorawan-devices
