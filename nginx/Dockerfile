FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/

RUN groupadd -g 1002 nginx-certs
RUN useradd -r -u 1014 -g nginx-certs nginx-certs

RUN chown -R nginx-certs:nginx-certs /var/cache/nginx && \
        chown -R nginx-certs:nginx-certs /var/log/nginx && \
        chown -R nginx-certs:nginx-certs /etc/nginx/conf.d
RUN touch /var/run/nginx.pid && \
        chown -R nginx-certs:nginx-certs /var/run/nginx.pid

USER 1014:1002
