FROM nginx:1.21

COPY ./nginx.conf /etc/nginx/nginx.conf

# Generate self-signed SSL certificate
COPY ./openssl.cnf ./openssl.cnf

RUN openssl req -new -newkey rsa:4096 -nodes -x509 \
    -config openssl.cnf \
    -keyout /etc/nginx/localhost.key \
    -out /etc/nginx/localhost.crt
