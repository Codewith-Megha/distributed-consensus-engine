#!/bin/bash

echo "Stopping Node 3"

docker stop node3

sleep 10

echo "Starting Node 3"

docker start node3