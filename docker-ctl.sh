#!/bin/bash
#[WARNING] Do not run this...Unless.
#Desctiption: Stop or Remove all Docker Containers from this system. 
function docker-stop(){
   echo "STOP ALL containers"
   docker ps -a | awk '{ print $1 }' | grep -v CONTAINER | xargs -I{} docker stop {}
}
function docker-rm(){
   echo "REMOVE ALL containers"
   docker ps -a | awk '{ print $1 }' | grep -v CONTAINER | xargs -I{} docker rm {}
}
while [ true ]; do
   echo "Docker Actions:"
   echo "1. Remove all containers..Deleting them forever"
   echo "2. Stop all containers"
   echo "3. Exit this loop"
   read answer
   case $answer in
      1) echo "Execute Delete All Containers"; docker-rm  ;;
      2) echo "Execute Stop All Containers"; docker-stop  ;;
      3) echo "Exiting."; break                           ;;
      *) echo "Please use numerical menu choice."; break  ;;
   esac 
done
