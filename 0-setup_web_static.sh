#!/usr/bin/env bash
#a Bash script that sets up your web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "This is a test" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx start

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    apt-get update
    apt-get install -y nginx
fi

# Create necessary directories if they don't exist
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a fake HTML file for testing
echo "<html>
<head>
</head>
<body>
    Holberton School
</body>
</html>" > /data/web_static/releases/test/index.html

# Create or recreate the symbolic link
rm -rf /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current

# Set ownership of /data/ folder recursively to ubuntu user and group
chown -hR ubuntu:ubuntu /data/
sudo sed -i '/server_name _;/a \\n\tlocation /hbnb_static/{\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-enabled/default

sudo nginx -t

sudo service nginx restart
