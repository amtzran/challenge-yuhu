server {
    listen ${LISTEN_PORT};
    server_name ${DOMAIN};

    proxy_read_timeout 600;
    proxy_connect_timeout 600;
    proxy_send_timeout 600;

    location /static {
        alias /vol/static;
    }

    location /.well-known/acme-challenge/ {
        root /vol/www/;
    }

    location / {
        return 301 https://$host$request_uri;
    }
}