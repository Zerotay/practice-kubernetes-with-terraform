#!/usr/bin/bash

source /vagrant/cluster-init/init.sh

cat << 'EOF' | sudo tee /etc/default/kubelet
KUBELET_EXTRA_ARGS=--node-ip=192.168.56.10
EOF


OUTPUT_FILE=/vagrant/cluster-init/join.sh
rm -rf $OUTPUT_FILE
rm -rf /vagrant/.kube
sudo kubeadm init --pod-network-cidr=10.244.0.0/16 --control-plane-endpoint=192.168.56.10 --apiserver-advertise-address=192.168.56.10
sudo kubeadm token create --print-join-command > $OUTPUT_FILE
chmod +x $OUTPUT_FILE

mkdir -p $HOME/.kube
sudo cp /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
cp -R $HOME/.kube /vagrant/.kube
cp -R $HOME/.kube /home/vagrant/.kube
sudo chown -R vagrant:vagrant /home/vagrant/.kube
kubectl apply -f https://raw.githubusercontent.com/flannel-io/flannel/master/Documentation/kube-flannel.yml
kubectl completion bash >/etc/bash_completion.d/kubectl
echo 'alias k=kubectl' >>/home/vagrant/.bashrc

