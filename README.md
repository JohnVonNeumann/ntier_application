#ntier_application

## THE ROOT OF THE PROJECT DOES NOT RETURN A PAGE, THIS DOES NOT MEAN THE REST OF THE PROJECT IS BROKEN

## Setup steps
1. docker-compose build
2. docker-compose run web python3 manage.py migrate
3. docker-compose up
4. navigate to localhost/data/insert_data
5. Refresh a few times
6. navigate to localhost/data/select_data
7. ???
8. Profit

## Resources Used
1. https://docs.docker.com/compose/django/
2. https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html
3. https://github.com/dockerfiles/django-uwsgi-nginx/blob/master/Dockerfile
4. https://stackoverflow.com/questions/33992867/how-do-you-perform-django-database-migrations-when-using-docker-compose
5. https://docs.djangoproject.com/en/2.1/intro/tutorial01/

## Full Disclosure
> Due to my inexperience with Docker, I went through this challenge and worked through some of the kinks to develop a better understanding of what I was doing and the places I'd probably have issues, before actually attempting it, I regarded this as planning. Ultimately I learnt a let throughout this challenge, and I have really enjoyed Docker.

## Things that could be improved
1. Handle django migrations in a more Docker like way, I've seen people using separate containers to handle this.
2. Utilise uwsgi's emperor mode.
3. Make the data pages prettier, I'm no frontender lol.
4. The overall root index caused me issues with the entire page, so it looks ugly.
