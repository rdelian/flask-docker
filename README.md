# Flask App With Docker

## Info
Python 3.5 flask app template using docker.\
The project comes with SSL support ready, login/register and SqlAlchemy

## Pre-build
First you will need `platform_base_img` from [here]() to be able to build the project \
You have to configure your project `docker-compose.yml` and your own domain (if any) in `./init/platform.conf` 

## Config
- `MYSQL_ROOT_PASSWORD` & `MYSQL_DATABASE` database login info (_edit the ones from `platform_db` service as well_)
- `FLASK_ENV` has 2 modes **produciton** and **development**
    - `production` runs flask app with apache2
    - `development` runs flask in development mode


## Build
1. `cd flask-docker`
2. `docker-compose up -d --build`


