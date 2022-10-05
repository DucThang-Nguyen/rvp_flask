#!/bin/bash

docker image build -t rpn_flask:latest --no-cache .
docker container run -it -p 5000:5000 rpn_flask:latest