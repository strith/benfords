FROM python:3.8-slim

COPY . /var/www
WORKDIR /var/www
RUN chown -R www-data:www-data /var/www

RUN apt-get update

RUN apt-get -y install nginx python3-dev build-essential

RUN pip install -r requirements.txt --src /usr/local/src

COPY nginx.conf /etc/nginx
RUN chmod +x ./start.sh

CMD ["./start.sh"]
