#!/bin/bash

set -o errexit
set -o nounset

cp /home/ubuntu/.env /home/ubuntu/www/project/
cd /home/ubuntu/www/project/
echo "Deploying application in ${ENVIRONMENT}"
if [ ${ENVIRONMENT} == 'production' ]
then
    docker-compose -f docker-compose-prod.yml up -d --build
else
    docker-compose up -d --build
fi
echo "Application in ${ENVIRONMENT} is deployed"