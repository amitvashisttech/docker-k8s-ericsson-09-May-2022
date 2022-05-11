```
  756  kubectl  get pods -n kube-system 
  757  vim /etc/kubernetes/kubelet.conf 
  758  vim /var/lib/kubelet/config.yaml 
  760  vim /etc/kubernetes/manifests/kube-apiserver.yaml 

  761  kubectl  cluster-info
  762  kubectl cluster-info dump
  763  kubectl  version
  764  kubectl  api-resources
  765  kubectl  api-versions
  766  curl http://172.31.0.100:6443
  767  curl -k https://172.31.0.100:6443
  768  kubectl proxy --address='172.31.0.100' --port=8080 --accept-hosts='.' --accept-paths='.' & 
  769  curl localhost
  770  curl localhost:8080
  771  kubectl proxy --address='172.31.0.100' --port=8080 --accept-hosts='.' --accept-paths='.' & 
  772  curl 172.31.0.100:8080
  773  curl 172.31.0.100:8080/api
  774  curl 172.31.0.100:8080/apis
  775  curl 172.31.0.100:8080/api/v1 
  776  curl 172.31.0.100:8080/api/v1/pods 
  777  kubectl  get pods 
  778  kubectl  get pods -o wide 
  779  kubectl config view 
  780  kubectl config get-clusters
  781  kubectl config get-clusters kubernetes
  782  kubectl config view 
  783  kubectl  config get-contexts 
  784  ls
  785  cd docker-k8s-ericsson-09-May-2022/
  786  ls
  787  cd 02-K8s/
  788  ls
  789  mkdir 03-Kube-Api
  790  cd 03-Kube-Api/
  791  history > README.md
```
