Write-Host "build the docker-compose apps" -ForegroundColor Yellow
Write-Host "docker-compose build" -ForegroundColor Green
docker-compose build

Write-Host "start the docker-compose apps (will build if not built, but docker-compose build should be used when changes are made)" -ForegroundColor Yellow
Write-Host "docker-compose up" -ForegroundColor Green
docker-compose up

docker rm -f $(docker ps -aq)

Write-Host "run a single app from the docker-compose file" -ForegroundColor Yellow
Write-Host "docker-compose up app1" -ForegroundColor Green
docker-compose up app1

docker rm -f $(docker ps -aq)

Write-Host "Would push containers to username/repository specified in docker files (will  only run if images are built)" -ForegroundColor Yellow
Write-Host "docker-compose push" -ForegroundColor Green

docker rmi -f $(docker images -aq)

