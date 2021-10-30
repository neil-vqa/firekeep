#! /usr/bin/sh

autoflake --in-place --recursive firekeep && isort firekeep && black firekeep \
&& export FLASK_APP=firekeep:app && export FLASK_ENV=development && flask run