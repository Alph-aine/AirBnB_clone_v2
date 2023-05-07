#!/usr/bin/env bash
# a script that sets up web servers for the deployment of web_static

if ! [ -x "$(command -v nginx)" ]; then
	sudo apt-get -y update
	sudo apt-get -y install nginx
fi

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo echo -e "<html>\n <head>\n </head>\n <body>\n  Holberton School\n </body>\n</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sed -i '/listen 80 default_server;/a location /hbnb_static/ {\n\talias /data/web_static/current/;\n\tindex index.html;\n}\n' /etc/nginx/sites-enabled/default
sudo service nginx start
