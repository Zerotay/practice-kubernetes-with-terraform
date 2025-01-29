
# install metric server

# install metallb
kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.14.9/config/manifests/metallb-native.yaml

cat <<EOL | kubectl apply -f -
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  name: ip-pool
  namespace: metallb-system
spec:
  addresses:
  - 192.200.0.0/24
---
apiVersion: metallb.io/v1beta1
kind: L2Advertisement
metadata:
  name: l2ad
  namespace: metallb-system
spec:
  ipAddressPools:
  - ip-pool
EOL
