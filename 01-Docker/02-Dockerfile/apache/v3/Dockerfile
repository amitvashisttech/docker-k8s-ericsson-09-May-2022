# Base Image
FROM ubuntu:16.04 

# Update the APT Repo 
RUN apt-get update 

# Install Apache Packages 
RUN apt-get install apache2 -y 

# Deploy Custom Web Page
COPY index.html /var/www/html/

# Expose the Port
EXPOSE 80 

# Bring the Apache UP 
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
