# Django REST and Vite ReactJS

Boiler plate code to get started on full stack applications fast.
Includes auth, basic models, and protected routes.

# Steps to get running

## Installation
1. Install docker and docker-compose

The docker software can be downloaded here:
https://www.docker.com/products/docker-desktop/

To install docker-compose on Linux:

```
sudo curl -L "https://github.com/docker/compose/releases/download/v2.5.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

```
sudo chmod +x /usr/local/bin/docker-compose
```

check installation
```
docker-compose --version
```

2. Clone this repository.

## Running the dev server

3. Create an `.env` file in the backend directory with `touch .env`

Some typical backend environment variables could be:
```
SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=mydatabase
DB_USER=myuser
DB_PASSWORD=mypassword
DB_HOST=db
DB_PORT=5432
```

4. Create an `.env` file in the frontend directort with `touch .env`

Some typical frontend environment variables could be:
```
REACT_APP_API_URL="http://127.0.0.1:8000"
NODE_ENV=development
```

5. Build the docker image. You may need to add `sudo` on Linux.

```
docker-compose build
```

6. Start the docker container. (again, you may need `sudo` for Linux)

```
docker-compose up
```

7. In another terminal window, but while the first one is still running, make migrations and migrate. (if you're on Linux and you've gotten to this point do I really need to mention `sudo`?)

```
docker-compose exec web python manage.py makemigrations
```

```
docker-compose exec web python manage.py migrate
```

8. Seed the db (if seed data exists)
```
docker-compose exec web python manage.py loaddata seed_data.json
```

9. Create a superuser
```
docker-compose exec web python manage.py createsuperuser
```

10. Collect static files (css, js, images)
```
docker-compose exec web python manage.py collectstatic
```

**NOTE** The homepage is protected by default. This is just so that there's something there. 