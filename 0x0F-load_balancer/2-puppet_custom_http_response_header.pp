# Web server Configs with HTTP header response.

# Install Nginx
package { 'nginx':
  ensure => 'installed',
}

# Redirection Configuration
file { '/etc/nginx/sites-enabled/default':
  ensure  => file,
  content => "server {\n  server_name _;\n  rewrite ^/redirect_me https://github.com/VloneMe permanent;\n}",
  notify  => Service['nginx'],
}

file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
}

# Create a custom 404 Not Found page
file { '/var/www/html/custom_404.html':
  ensure  => file,
  content => "Ceci n'est pas une page",
}

# Add "Hello, World!" to index.html
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello, World!',
}

# Configure Nginx to use the custom 404 page
file { '/etc/nginx/sites-enabled/default':
  ensure  => file,
  content => "server {\n  listen 80 default_server;\n  error_page 404 /custom_404.html;\n  location = /custom_404.html {\n    root /var/www/html;\n    internal;\n  }\n}",
  notify  => Service['nginx'],
}

# Create a custom HTTP response header
file_line { 'custom_header':
  path    => '/etc/nginx/sites-available/default',
  line    => '    server_name _;',
  match   => '    server_name _;',
  after   => '    server_name _;',
  content => '    add_header X-Served-By $HOSTNAME;',
  notify  => Service['nginx'],
}

# Restart Nginx to apply changes
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => [
    File['/etc/nginx/sites-available/default'],
    File['/var/www/html/custom_404.html'],
    File['/var/www/html/index.html'],
  ],
}
