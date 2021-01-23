FROM nginx:1.17.2-alpine


RUN rm /etc/nginx/conf.d/default.conf
WORKDIR /etc/nginx/
COPY portfolio_django.conf ./conf.d
WORKDIR /