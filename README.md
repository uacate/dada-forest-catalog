# DADA-Forest

## Deployment tasks
git pull
docker exec -it catalog_app ./manage.py collectstatic
docker exec -it catalog_app ./manage.py migrate