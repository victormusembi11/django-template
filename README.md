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
pip install -r requirements.txt
```

## Run migrations

```bash
python manage.py migrate
```

## Run server

```bash
python manage.py runserver
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
