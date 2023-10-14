FROM nginx

RUN rm /etc/nginx/conf.d/default.conf

RUN useradd -r -u 1004 -g nginx nginx
USER nginx

COPY nginx.conf /etc/nginx/conf.d/