FROM nginx

RUN rm /etc/nginx/conf.d/default.conf

RUN groupadd -g 1002 nginx-certs
RUN useradd -r -u 1014 -g nginx-certs nginx-certs
USER 1014:1002

COPY nginx.conf /etc/nginx/conf.d/