  480  echo "************************** Docker Volumes ************************" 
  481  docker volume ls 
  482  docker volume create my-vol
  483  docker volume ls 
  484  docker volume inspect my-vol 
  485  docker run -it --name vol-test-1 -v my-vol:/app ubuntu:16.04 
  486  docker ps 
  487  docker inspect vol-test-1
  488  cat /var/lib/docker/volumes/my-vol/_data/
  489  cat /var/lib/docker/volumes/my-vol/_data/hello.txt 
  490  hostname >> /var/lib/docker/volumes/my-vol/_data/hello.txt
  491  date >> /var/lib/docker/volumes/my-vol/_data/hello.txt
  492  docker ps 
  493  docker attach vol-test-1
  494  docker kill $(docker ps -q) 
  495  docker rm $(docker ps -aq) 
  496  docker ps -a 
  497  docker volume ls 
  498  cat /var/lib/docker/volumes/my-vol/_data/hello.txt 
  499  docker run -it --name vol-test-2 -v my-vol:/app ubuntu:16.04 
  500  docker run -it --name vol-test-3 -v /var/www/amit ubuntu:16.04 
  501  docker volume ls 
  502  docker inspect vol-test-3
  503  cat /var/lib/docker/volumes/8dda34b4e11eb8257b89c9fe6e862e1405d48ff4a98589c78e5562bc7ef0171d/_data/abc.txt 
  504  docker run -it --name vol-test-4 -v /var/www/amit -v /etc/amit -v /var/log/amit ubuntu:16.04 
  505  docker ps 
  506  docker inspect vol-test-4
  507  ls
  508  pwd
  509  docker run -it --name vol-test-5 -v /root/docker-k8s-ericsson-09-May-2022:/myapp ubuntu:16.04 
  510  ls
  511  cd 01-Docker/
  512  ls
  513  cat hello_from_container.txt 
  514  pwd
  515  cd ..
  516  ls
  517  docker run -it --name vol-test-6 -v /root/docker-k8s-ericsson-09-May-2022:/myapp:ro ubuntu:16.04 
  518  docker run -itd --name data-vol -v /var/www/amit -v /etc/amit -v /var/log/amit ubuntu:16.04 
  519  docker ps 
  520  docker run -itd --name data-vol-test-1 --volumes-from data-vol ubuntu:16.04 
  521  docker run -itd --name data-vol-test-2 --volumes-from data-vol ubuntu:16.04 
  522  docker run -itd --name data-vol-test-3 --volumes-from data-vol ubuntu:16.04 
  523  docker ps 
  524  docker attach data-vol-test-1
  525  docker exec -it data-vol-test-1 cat /etc/amit/hello.txt 
  526  docker exec -it data-vol-test-2 cat /etc/amit/hello.txt 
  527  docker exec -it data-vol-test-3 cat /etc/amit/hello.txt 
  528  docker ps 
  529  docker stop data-vol
  530  docker rm data-vol
  531  docker ps 
  532  docker ps -a
  533  docker exec -it data-vol-test-3 cat /etc/amit/hello.txt 
  534  ls
  535  cd 01-Docker/
  536  ls
  537  mkdir 03-DockerVolumes 
  538  history 03-DockerVolumes/README.md
  539  history > 03-DockerVolumes/README.md
