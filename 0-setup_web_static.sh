#!/usr/bin/env bash
#a Bash script that sets up your web servers for the deployment of web_static

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
    <title>Home - AirBnB Clone</title>
</head>
<body>
    <h1>Welcome to AirBnB!</h1>
</body>
</html>" > /data/web_static/releases/test/index.html

# Create or recreate the symbolic link
rm -rf /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current

# Set ownership of /data/ folder recursively to ubuntu user and group
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_file="/etc/nginx/sites-available/default"

# Remove existing "location /hbnb_static" block if present
sed -i '/location \/hbnb_static {/,/}/d' "$config_file"

# Add new "location /hbnb_static" block to the configuration
echo "
location /hbnb_static {
    alias /data/web_static/current/;
    index index.html;
}" >> "$config_file"

# Restart Nginx to apply the configuration changes
service nginx restart

exit 0
