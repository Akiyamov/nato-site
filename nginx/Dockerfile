FROM nginx

RUN rm /etc/nginx/conf.d/default.conf

RUN groupadd nginx-certs
RUN useradd -r -u 1014 -g nginx-certs nginx-certs
USER nginx

COPY nginx.conf /etc/nginx/conf.d/