#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static. 

# Update package lists and install nginx
if ! dpkg -l | grep -q nginx; then
    echo "[+] Package not installed. Installing..."
    sudo apt-get update && sudo apt-get install nginx -y
else
    echo "[+] Nginx already installed."
fi

# Create folders in they did not exist
folders=("/data/" "/data/web_static/" "data/web_static/releases" 
	 "/data/web_static/shared/" "/data/web_static/releases/test/")

for folder in folders; do
	if [ ! -d "$folder" ]; then
		mkdir -p "$folder"
		echo "[+] Folder $folder created successfully."
	else
		echo "[+] Folder $folder already exists."
	fi
done

# paths
releases_path="/data/web_static/releases"
test_path="${releases_path}/test/"
current_path="/data/web_static/current"
html_file="${test_path}/index.html"

#create a simple html file for testing
echo "<html><body><h1>Test HTML File</h1><body></html>" > "$html_file"

#creating a symbolic link
if [ -L "$current_path" ]; then
	rm "$current_path"
	echo "[-] Link already exists"
fi

ln -sF "$test_path" "$current_path"
echo "[+] Symbolic link created"

# change ownership recursively
chown -R ubuntu:ubuntu /data/

# Remove the default Nginx config files
rm -rf /etc/nginx/sites-available/default
rm -rf /etc/nginx/sites-enabled/default

# Create a new configuration file
cat > /etc/nginx/sites-available/default.conf << EOF
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    location /hbnb_static/ {
        alias /data/web_static/current/;
        index index.html;
    }

    server_name _;

    add_header X-Served-By $HOSTNAME;

    location / {
        try_files \$uri \$uri/ =404;
    }

    location /redirect_me {
        return 301 https://google.com;
    }

    error_page 404 /404.html;

    location = /404.html {
        internal;
        add_header Content-Type text/html;
        return 404 "Ceci n'est pas une page";
    }
}
EOF

# Enable the new configuration file
ln -s /etc/nginx/sites-available/default.conf /etc/nginx/sites-enabled/

# Create the /var/www/html directory if it doesn't exist
mkdir -p /var/www/html

# Create the index.html file
echo "Hello World!" > /var/www/html/index.html

sudo service nginx restart
