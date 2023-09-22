# Creates A  puppet Manifest for creating a file in /tmp

# This ensures that the directory /tmp exists
# If not will create it.
file { '/tmp':
  ensure => 'directory',
}

# This creates the /tmp/school file 
# with the specified permissions, owner, group, and content
file { '/tmp/school':
  ensure  => 'file',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
