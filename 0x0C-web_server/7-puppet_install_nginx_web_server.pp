# A class for Nginx installation and configuration

class nginx_config {

  # This Installing Nginx package
  package { 'nginx':
    ensure => 'installed',
  }

  # This defines Nginx site configuration
  file { '/etc/nginx/sites-available/default':
    content => template('nginx_config/nginx.erb'),
    require => Package['nginx'],
  }

  # This will enable the Nginx site
  file { '/etc/nginx/sites-enabled/default':
    ensure => 'link',
    target => '/etc/nginx/sites-available/default',
    require => File['/etc/nginx/sites-available/default'],
  }

  # This ensures that Nginx service is running and enabled
  service { 'nginx':
    ensure  => 'running',
    enable  => true,
    require => [Package['nginx'], File['/etc/nginx/sites-enabled/default']],
  }

}

# This apply the class to the node
node 'francisntima.tech' {
  include nginx_config
}
