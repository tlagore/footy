# return

# docker stack ls                                            # List stacks or apps
# docker stack deploy -c <composefile> <appname>  # Run the specified Compose file
# docker service ls                 # List running services associated with an app
# docker service ps <service>                  # List tasks associated with an app
# docker inspect <task or container>                   # Inspect task or container
# docker container ls -q                                      # List container IDs
# docker stack rm <appname>                             # Tear down an application
# docker swarm leave --force      # Take down a single node swarm from the mana


#swarm stuff
#manager
docker swarm init
#workers
docker swarm join

# create VMs (when not running Hyper-V)
docker-machine create --driver virtualbox myvm1
docker-machine create --driver virtualbox myvm2

#when running Hyper-V
docker-machine create -d hyperv --hyperv-virtual-switch "myswitch" myvm1
docker-machine create -d hyperv --hyperv-virtual-switch "myswitch" myvm2