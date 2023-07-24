#!/usr/bin/env bash
# configures nginx as a web server

# checks if nginx is already installed or installs it

if ![  dpkg -l nginx &> /dev/null ]; then
  sudo apt update
  sudo apt install nginx -y
fi 

mkdir -p /data/
mkdir -p /data/web_static
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "Hello world!" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/  /data/web_static/current
sudo chown -R  ubuntu:ubuntu /data/
sed -i '/listen 80 default_server;/a location /hbnb_static/ {\n\talias /data/web_static/current/;\n\tindex index.html;\n}\n' /etc/nginx/sites-enabled/default
sudo service nginx start
