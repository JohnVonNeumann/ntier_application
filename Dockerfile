FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
RUN apt update
RUN apt-get install nginx -y
RUN sed -i "3i daemon off;" /etc/nginx/nginx.conf
COPY mysite_nginx.conf /etc/nginx/sites-available/default
RUN apt install supervisor -y
COPY supervisor-app.conf /etc/supervisor/conf.d/
CMD ["supervisord", "-n"]
