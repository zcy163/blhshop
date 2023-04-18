#!/bin/sh
# override redis entrypoint，使用root启动服务
set -e

# first arg is `-f` or `--some-option`
# or first arg is `something.conf`
if [ "${1#-}" != "$1" ] || [ "${1%.conf}" != "$1" ]; then
	set -- redis-server "$@"
fi


if [ "$1" = 'redis-server' -a "$(id -u)" != '0' ]; then
	exec gosu root "$0" "$@"
fi

exec "$@"