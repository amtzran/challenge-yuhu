# Starter Project Backend

Commands:

```shell
make dev
```
Goes to dev branch and update last changes (migrate and install packages).

```shell
make migrations
```
python manage.py makemigrations
```shell
make migrate
```
python manage.py migrate

```shell
make check
```
Run tests, check migrations and format for github action and local review
```shell
make test
```
Run tests for server side

```shell
make format
```
Auto format with brunette (black).

```shell
make ilocal
```
Running commands with docker.

```shell
docker-compose run --rm app sh -c "python manage.py makemigrations"
```

```shell
docker-compose run --rm app sh -c "python manage.py migrate name-app zero"
```

Install environment packages (local or production).


## Running this project.

- Create and activate virtual environment.
- Copy /.env.sample as app/core/.env
- Copy /.env.sample as /.env
- Run ```make dev```

