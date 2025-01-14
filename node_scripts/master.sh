#!/bin/bash
#
# Setup for Control Plane (Master) servers
set -euxo pipefail
NODENAME=$(hostname -s)

#!/usr/bin/bash
OUTPUT_FILE=/vagrant/node_scripts/join.sh
rm -rf $OUTPUT_FILE
rm -rf /vagrant/.kube
# sudo kubeadm init --pod-network-cidr=10.244.0.0/16 --control-plane-endpoint=192.168.56.10 --apiserver-advertise-address=192.168.56.10
sudo kubeadm init --config /vagrant/node_scripts/kubeadm-config.yaml
sudo kubeadm token create --print-join-command > $OUTPUT_FILE
chmod +x $OUTPUT_FILE
echo $OUTPUT_FILE

mkdir -p $HOME/.kube
sudo cp /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
cp -R $HOME/.kube /vagrant/.kube
cp -R $HOME/.kube /home/vagrant/.kube
sudo chown -R vagrant:vagrant /home/vagrant/.kube
kubectl completion bash >/etc/bash_completion.d/kubectl
echo 'alias k=kubectl' >>/home/vagrant/.bashrc
echo 'complete -o default -F __start_kubectl k' >>/home/vagrant/.bashrc
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

# network setting
# kubectl apply -f https://raw.githubusercontent.com/flannel-io/flannel/master/Documentation/kube-flannel.yml
kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml

# Install Metrics Server
kubectl apply -f https://raw.githubusercontent.com/techiescamp/kubeadm-scripts/main/manifests/metrics-server.yaml

# storage setting
helm repo add csi-driver-nfs https://raw.githubusercontent.com/kubernetes-csi/csi-driver-nfs/master/charts
helm install csi-driver-nfs csi-driver-nfs/csi-driver-nfs --namespace kube-system --version v4.9.0
# kubectl apply -f - <<EOF
# apiVersion: storage.k8s.io/v1
# kind: StorageClass
# metadata:
#   name: nfs-csi
# provisioner: nfs.csi.k8s.io
# parameters:
#   server: 192.168.56.9
#   share: /nfs/csi
#   # csi.storage.k8s.io/provisioner-secret is only needed for providing mountOptions in DeleteVolume
#   # csi.storage.k8s.io/provisioner-secret-name: "mount-options"
#   # csi.storage.k8s.io/provisioner-secret-namespace: "default"
# reclaimPolicy: Delete
# volumeBindingMode: Immediate
# mountOptions:
#   - nfsvers=4.1
# EOF


