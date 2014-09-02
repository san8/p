#!/bin/bash

cd /media/Extra/Project

tab=" --tab-with-profile=Default"
options=(--tab --title=Terminal)

cmds[1]="'rails s'"
titles[1]="Server"

cmds[2]="'rails c'"
titles[2]="Console"


for i in 1 2; do
  options+=($tab --title="${titles[i]}"  -e "bash -c \"${cmds[i]} ; bash\"" )          
done

terminator "${options[@]}"


exit 0
