# dev
docker-compose -f docker-compose-dev.yml --env-file .env.dev up -d
docker-compose -f docker-compose-prod.yml --env-file .env.prod up -d