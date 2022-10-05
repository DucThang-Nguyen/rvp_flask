#!/bin/bash
flask db migrate
flask db upgrade

pytest .
python ./wsgi.py