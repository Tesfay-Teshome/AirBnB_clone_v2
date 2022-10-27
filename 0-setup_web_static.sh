#!/usr/bin/env bash
# Prepare Web Server
apt-get update -y
apt-get install nginx -y
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "Holberton School" > /data/web_static/releases/test/index.html
rm -rf /data/web_static/current
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/

loc="\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n"

sudo sed -i "38i $loc" /etc/nginx/sites-available/default
service nginx restart
exit 0
