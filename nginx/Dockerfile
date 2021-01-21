FROM nginx:1.17.2-alpine

RUN mkdir /home/runner/work/AbhishekPortfolio/AbhishekPortfolio/postgres_data

RUN rm /etc/nginx/conf.d/default.conf
COPY portfolio_django.conf /etc/nginx/conf.d
