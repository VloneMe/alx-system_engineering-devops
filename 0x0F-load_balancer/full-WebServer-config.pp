# Web server Configs with HTTP header response.

# Install Nginx
exec { "Installing nginx":
	command => 'sudo apt-get -y update && sudo apt-get install -y nginx',
	provider => shell
}

# Redirection Configuration
exec { 'Redirection Configuration':
	command => 'sudo sed -i "s|server_name _|server_name _;\\n\\trewrite ^/redirect_me https://github.com/VloneMe permanent|g" /etc/nginx/sites-enabled/default',
	provider => shell
}

# Add "Hello, World!" to index.html
file { '/var/www/html/index.html':
  	ensure  => 'file',
  	content => "Hello, World!\n",
}

# Create a custom 404 Not Found page
file { '/var/www/html/custom_404.html':
  	ensure  => 'file',
  	content => "Ceci n'est pas une page\n",
}

# Configure Nginx to use the custom 404 page
exec { 'Nginx Custom Configuration':
  	command => 'sudo sed -i "s|listen 80 default_server;|listen 80 default_server;\\n\terror_page 404 /custom_404.html;\\n\tlocation = /custom_404.html {\\n\t\troot /var/www/html;\\n\t\tinternal;\\n\t}|g" /etc/nginx/sites-enabled/default',
  	path    => ['/usr/bin', '/bin'],
}

# Check Nginx configuration for syntax errors
exec { 'Check Nginx Configuration':
  	command => 'sudo nginx -t',
	provider => shell
}

# Add a custom HTTP header to the Nginx configuration
exec { 'HTTP header Response':
	command => 'sudo sed -i "/server_name _/a add_header X-Served-By \$HOSTNAME;" /etc/nginx/sites-enabled/default',
	provider => shell
}

# Restart Nginx to apply the changes
exec { 'Restarting nginx':
  command => 'sudo service nginx restart',
  provider => shell,
}
