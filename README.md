#ntier_application

## Setup steps

docker-compose build
docker-compose run web python3 manage.py migrate
docker-compose up
