# Setting up NFS Server for K8s PV Demo. 

## Install Nfs Server 
```
apt-get install nfs-kernel-server -y 
mkdir /myexports
chown nobody:nogroup /myexports
```

## Edit the NFS Export file (/etc/exports) & make the following entry. 
```
/myexports  *(rw,sync,no_subtree_check)
```

```
root@kube-master:~/k8s-paypal-28-Dec-2020/26-Volumes-NFS# grep -i exports /etc/exports
/myexports  *(rw,sync,no_subtree_check)
root@kube-master:~/k8s-paypal-28-Dec-2020/26-Volumes-NFS#
```

## Restart the NFS Server Service
```
systemctl restart nfs-kernel-server
systemctl status  nfs-kernel-server
```

## Vertify the NFS Share
```
showmount -e localhost 
```


# On Clinet / Worker Nodes 

## Install NFS Clinet Utils 
```
apt-get install nfs-common -y
mount -t nfs 172.31.0.10:/myexports /mnt/
cd /mnt/
hostname >> hostname.txt
```
