import-device-profiles:
	docker compose run --rm --entrypoint sh --user root chirpstack -c '\
		apk add --no-cache git && \
		git clone https://github.com/chirpstack/chirpstack-device-profiles.git /tmp/chirpstack-device-profiles && \
		chirpstack -c /etc/chirpstack import-device-profiles -d /tmp/chirpstack-device-profiles'
