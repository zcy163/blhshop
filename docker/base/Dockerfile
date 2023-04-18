FROM rockylinux:8

ARG CONTAINER_HOMEWORK
ENV CONTAINER_HOMEWORK $CONTAINER_HOMEWORK

ARG COMPOSE_PROJECT_NAME
ENV COMPOSE_PROJECT_NAME $COMPOSE_PROJECT_NAME

ARG SERVER_PROJECT_NAME
ENV SERVER_PROJECT_NAME $SERVER_PROJECT_NAME

# 切换镜像源
RUN sed -e 's|^mirrorlist=|#mirrorlist=|g' \
    	-e 's|^#baseurl=http://dl.rockylinux.org/$contentdir|baseurl=https://mirrors.aliyun.com/rockylinux|g' \
    	-i.bak \
    	/etc/yum.repos.d/Rocky-*.repo
RUN dnf makecache
# 更新和依赖安装
RUN yum update -y
RUN yum -y install gcc make cmake zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel xz xz-devel libffi-devel
RUN yum -y install nginx wget gettext mysql-devel

# 安装Python-3.10.6
RUN wget https://baiyu.bj.bcebos.com/Python-3.10.6.tgz -O /usr/local/src/Python-3.10.6.tgz
RUN tar zxvf /usr/local/src/Python-3.10.6.tgz --directory=/tmp
WORKDIR /tmp/Python-3.10.6
RUN /tmp/Python-3.10.6/configure
RUN make && make install
ENV LC_ALL=en_US.UTF-8

# 单独安装 uwsgi 和 supervisor
COPY docker/base/pip.conf ~/.pip/pip.conf
RUN pip3 install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip3 install supervisor==4.2.4 uwsgi==2.0.20 -i https://pypi.tuna.tsinghua.edu.cn/simple

# install python dependencies
COPY $SERVER_PROJECT_NAME/requirements.txt $CONTAINER_HOMEWORK/$COMPOSE_PROJECT_NAME/requirements.txt
RUN pip3 install -r $CONTAINER_HOMEWORK/$COMPOSE_PROJECT_NAME/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 安装node-v14.19.2
RUN wget https://baiyu.bj.bcebos.com/node-v14.19.2-linux-x64.tar.gz -O /usr/local/src/node-v14.19.2-linux-x64.tar.gz
RUN tar zxvf /usr/local/src/node-v14.19.2-linux-x64.tar.gz --directory=/tmp
RUN mv /tmp/node-v14.19.2-linux-x64/ /usr/local/nodejs
RUN ln -s /usr/local/nodejs/bin/npm /usr/local/bin/
RUN ln -s /usr/local/nodejs/bin/node /usr/local/bin/

# 改变npm默认的路径
RUN mkdir ~/.npm-global
RUN npm config set prefix '~/.npm-global'
RUN export PATH=~/.npm-global/bin:$PATH
# 更换npm镜像源
RUN npm config set registry https://registry.npm.taobao.org

# create run and log directory
RUN mkdir -p $CONTAINER_HOMEWORK/log/supervisord/uwsgi
RUN mkdir -p $CONTAINER_HOMEWORK/log/supervisord/nginx
RUN mkdir -p $CONTAINER_HOMEWORK/log/supervisord/eventhub
RUN mkdir -p $CONTAINER_HOMEWORK/log/nginx/
RUN mkdir -p $CONTAINER_HOMEWORK/log/uwsgi/
RUN mkdir -p $CONTAINER_HOMEWORK/log/$SERVER_PROJECT_NAME/
RUN mkdir -p $CONTAINER_HOMEWORK/run/

# copy entrypoint.sh
COPY docker/base/entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh

# copy supervisor conf
COPY docker/base/supervisor.conf $CONTAINER_HOMEWORK/deploy/supervisor.conf
RUN mkdir /etc/supervisor
RUN ln -s $CONTAINER_HOMEWORK/deploy/supervisor.conf /etc/supervisor/supervisord.conf

# copy uwsgi conf
COPY docker/base/uwsgi.ini $CONTAINER_HOMEWORK/deploy/uwsgi.ini

WORKDIR $CONTAINER_HOMEWORK/$COMPOSE_PROJECT_NAME/$SERVER_PROJECT_NAME
