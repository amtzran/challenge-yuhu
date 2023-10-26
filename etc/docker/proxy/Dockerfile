FROM nginx:1.23.0-alpine
LABEL maintainer="alberto.sofalm@gmail.com"

COPY ./nginx/* /etc/nginx/
COPY run.sh /run.sh

ENV LISTEN_PORT=80
ENV APP_HOST=app
ENV APP_PORT=9000

USER root

RUN apk add --no-cache openssl bash
RUN chmod +x /run.sh

VOLUME /vol/static
VOLUME /vol/www

CMD ["/run.sh"]