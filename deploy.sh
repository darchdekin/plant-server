#!/usr/bin/bash
KEYPATH="{}"
DNS="{user}@{dns}.amazon.com"

ssh -i $KEYPATH $DNS "docker stop \$(docker ps | grep darchdekin/plant-server | awk '{print \$1}'); docker pull darchdekin/plant-server; docker run -d -p 8000:8000 darchdekin/plant-server"