
FROM blhshop-base

ARG CONTAINER_HOMEWORK
ENV CONTAINER_HOMEWORK $CONTAINER_HOMEWORK

ARG COMPOSE_PROJECT_NAME
ENV COMPOSE_PROJECT_NAME $COMPOSE_PROJECT_NAME

ARG CONTAINER_USER
ENV CONTAINER_USER $CONTAINER_USER

ARG CONTAINER_GROUP
ENV CONTAINER_GROUP $CONTAINER_GROUP

RUN groupadd -g $CONTAINER_GROUP game
RUN useradd -u $CONTAINER_USER -g game game

RUN chown -R game:game /var/lib/nginx
RUN chown -R game:game /var/log/nginx

# copy nginx conf template
COPY docker/server/nginx.conf.template $CONTAINER_HOMEWORK/deploy/nginx.conf.template
# 使用环境变量创建nginx conf文件
RUN envsubst '{{ $CONTAINER_HOMEWORK $COMPOSE_PROJECT_NAME }}' < $CONTAINER_HOMEWORK/deploy/nginx.conf.template > $CONTAINER_HOMEWORK/deploy/nginx.conf
RUN rm /etc/nginx/nginx.conf
RUN ln -s $CONTAINER_HOMEWORK/deploy/nginx.conf /etc/nginx/nginx.conf

COPY . $CONTAINER_HOMEWORK/$COMPOSE_PROJECT_NAME
#RUN pip3 install -r $CONTAINER_HOMEWORK/$COMPOSE_PROJECT_NAME/blhserver/requirements.txt
RUN chown -R $CONTAINER_USER:$CONTAINER_GROUP $CONTAINER_HOMEWORK

USER $CONTAINER_USER

# run entrypoint.sh
#ENTRYPOINT ["/entrypoint.sh"]


