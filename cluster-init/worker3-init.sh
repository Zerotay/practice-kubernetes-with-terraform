#!/usr/bin/bash

source /vagrant/cluster-init/init.sh

cat << 'EOF' | sudo tee /etc/default/kubelet
KUBELET_EXTRA_ARGS=--node-ip=192.168.56.13
EOF

JOIN_FILE="/vagrant/cluster-init/join.sh"
source $JOIN_FILE
