FROM redis:6.2.6

COPY docker/redis/entrypoint.sh /entrypoint.sh
COPY docker/redis/healthcheck.sh /
COPY docker/redis/redis.conf /usr/local/etc/redis/redis.conf


#ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]

CMD ["redis-server", "/usr/local/etc/redis/redis.conf" ]