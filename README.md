# django-template

## Virtual environment setup

### Create virtual environment

```bash
python3 -m venv venv
```

### Activate virtual environment

```bash
source venv/bin/activate
```

## Environment variables setup

Create a `.env` file in the **root directory** and add the following variables in the .env.example file.

### Note

The default database is **sqlite3** on local environment. If you want to use postgresql(or any other), then make sure you set the environment variables in the .env for the database as shown in the .env.example file so that the **DB_IS_AVAIL** variable in **config.settings.local** is set to **True**.

## Install dependencies

```bash
pip install -r requirements/local.txt
```

## Run migrations

If you don't set the DB variables in the .env file, then the default database is sqlite3.

```bash
python manage.py migrate
```

## Run local server

```bash
python manage.py runserver
```

## Run tests

This covers linting with flake8, unit tests with pytest and coverage report.

```bash
tox
```

## Run production server

### Install dependencies

```bash
pip install -r requirements/production.txt
```

### Other Requirements

- AWS S3 bucket <https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html>
- AWS IAM user with access to the S3 bucket <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html>
- Sentry account <https://sentry.io/>
- Production database e.g. elephantSQL <https://www.elephantsql.com/>

### Note

Make sure you set the environment variables in the .env for the database as shown in the .env.example file so that the DATBASE_URL, AWS S3 variables & SENTRY variables are set.

```bash
python manage.py runserver --settings=config.settings.prod
```

## Docker setup

### Note

The default port for postgresql is **5432** but in the Docker setup, the port is **5435**. So, make sure you change the port number in the .env file when using Docker.

### Build image and run container

```bash
docker-compose up --build
```

### List images

```bash
docker images
```

### List containers

```bash
docker ps
```
