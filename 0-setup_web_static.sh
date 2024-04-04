#!/usr/bin/env bash
#script that sets up your web servers for the deployment of web_static.
#It Installs Nginx if it not already installed
#Create the folder /data/ if it doesn’t already exist
#Create the folder /data/web_static/ if it doesn’t already exist
#Create the folder /data/web_static/releases/ if it doesn’t already exist
#Create the folder /data/web_static/shared/ if it doesn’t already exist
#Create the folder /data/web_static/releases/test/ if it doesn’t already exist
#Create a fake HTML file /data/web_static/releases/test/index.html
#Create a symbolic link /data/web_static/current linked
#       to the /data/web_static/releases/test/ folder.
#Give ownership of the /data/ folder to the ubuntu user AND group
#Update the Nginx configuration to serve the content of
#     /data/web_static/current/ to hbnb_static
