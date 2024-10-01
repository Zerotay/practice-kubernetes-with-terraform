#!/usr/bin/bash

if [[ -z $1 ]]; then
  RESOURCE="pods"
else
  RESOURCE=$1
fi
if [[ -z $2 ]]; then
  NAMESPACE="default"
else
  NAMESPACE=$($2)
fi
echo $RESOURCE
echo $NAMESPACE
while true; do
  echo refresh for every 2 sec
  kubectl get -n $NAMESPACE $RESOURCE -o wide
  sleep 2
  clear
done
