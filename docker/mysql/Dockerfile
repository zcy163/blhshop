FROM mysql:8

# 初始化数据库
COPY docker/mysql/game.cnf /etc/mysql/conf.d/game.cnf
COPY docker/mysql/init/ /docker-entrypoint-initdb.d
