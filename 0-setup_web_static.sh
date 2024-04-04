#!/usr/bin/env bash
#script that sets up your web servers for the deployment of web_static.
#1) It Installs Nginx,
#2) Creates the folder /data/web_static/releases/test/,
#                     /data/web_static/shared/
#3) then Creates HTML file /data/web_static/releases/test/index.html
#4) then Creates a symbolic link /data/web_static/current ->
#                               /data/web_static/releases/test/
#5)Give ownership of the /data/ folder to the ubuntu user AND group
#6)Update the Nginx configuration to serve the content of
#     /data/web_static/current/ to hbnb_static
#7)restart nginx
if ! command -v nginx &> /dev/null; then
    sudo apt update
    sudo apt install -y nginx
else
    echo "Nginx is already installed."
fi

directories=(
    "/data/"
    "/data/web_static/"
    "/data/web_static/releases/"
    "/data/web_static/shared/"
    "/data/web_static/releases/test/"
)

for dir in "${directories[@]}"; do
    if [ ! -d "$dir" ]; then
        sudo mkdir "$dir"
    fi
done

sudo echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -hR ubuntu:ubuntu /data/

sudo sed -i '/server_name _;/a \\n\tlocation /hbnb_static/
{\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-enabled/default

sudo service nginx restart
