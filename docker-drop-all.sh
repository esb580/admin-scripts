#!/bin/bash
#WARNING: Don't run this unless you want to remove all your containers. 
#  That would be bad.
#Description: Remove all docker containers.  Too lazy to type.
docker ps -a | awk '{ print $1 }' | grep -v CONTAINER | xargs -I{} docker rm {}
