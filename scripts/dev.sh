#! /usr/bin/sh

isort firekeep && export FLASK_APP=firekeep:app && export FLASK_ENV=development && flask run