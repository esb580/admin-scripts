#!/bin/bash
#[WARNING] Do not run this...Unless.
#Description: Provide menu for things that take a long time to type.
#  This is a very dangerous script if you are using docker. 
function docker-stop(){
   echo "STOP ALL containers"
   docker ps -a | awk '{ print $1 }' | grep -v CONTAINER | xargs -I{} docker stop {}
}

function docker-rm(){
   echo "REMOVE ALL containers"
   docker ps -a | awk '{ print $1 }' | grep -v CONTAINER | xargs -I{} docker rm {}
}

function docker-rmi(){
   echo "REMOVE ALL images"
   docker images | awk '{ print $3 }' | grep -v IMAGE* | xargs -I{} docker rmi {}
}

while [ true ]; do
   echo "================================================"
   echo "Docker Actions:"
   echo "1. Remove all containers..Deleting them forever"
   echo "2. Stop all containers"
   echo "3. Remove all images"
   echo "4. Exit this loop"
   echo "================================================"
   read answer
   case $answer in
      1) echo "Execute Delete All Containers"; docker-rm  ;;
      2) echo "Execute Stop All Containers"; docker-stop  ;;
      3) echo "Remove all Docker Images"; docker-rmi      ;;
      4) echo "Exiting."; break                           ;;
      *) echo "Please use numerical menu choice."; break  ;;
   esac 
done
