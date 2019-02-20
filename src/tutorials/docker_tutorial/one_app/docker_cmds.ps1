param(
    #username of to access the repository
    [Parameter(Mandatory=$true)]
    [ValidateNotNullOrEmpty()]
    [string] $user,

    # repository name, a repository can have many apps through tags
    # example: footy_backend
    [Parameter(Mandatory=$true)]
    [ValidateNotNullOrEmpty()]    
    [string] $repository,

    # tag name, name of the app
    [Parameter(Mandatory=$true)]
    [ValidateNotNullOrEmpty()]
    [string] $tag
)

$image = "$user/$($repository):$tag"

docker build --tag=$image .

Write-Host "Run image" -ForegroundColor yellow
Write-Host "docker run $image" -ForegroundColor green
docker run $image

Write-Host "Run image detatched" -ForegroundColor Yellow
Write-Host "docker run -d $image" -ForegroundColor green
docker run -d $image

$cont2 = (docker ps --last 1 -q)
Write-Host "View live logs of running container $cont2 (note this is bugged currently and only shows after container exits)" -ForegroundColor Yellow
Write-Host "docker logs -f $cont2" -ForegroundColor green
docker logs -f $cont2

Write-Host "Stop containers" -ForegroundColor Yellow
Write-Host "docker stop $(docker ps -aq)" -ForegroundColor Green
docker stop $(docker ps -aq)

Write-Host "Remove containers" -ForegroundColor Yellow
Write-Host "docker rm -f $(docker ps -aq)" -ForegroundColor Green
docker rm -f $(docker ps -aq)

Write-Host "Remove images" -ForegroundColor Yellow
Write-Host "docker rmi -f $(docker images -aq)" -ForegroundColor Green
docker rmi -f $(docker images -aq)
