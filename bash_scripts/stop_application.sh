#!/bin/bash

set -o errexit
set -o nounset

cd /home/ubuntu/www/project/
echo "Stoping application in ${ENVIRONMENT}"
if [ ${ENVIRONMENT} == 'production' ]
then
    docker-compose -f docker-compose-prod.yml down --volumes
else
    docker-compose down --volumes
fi
echo "Application in ${ENVIRONMENT} stopped"