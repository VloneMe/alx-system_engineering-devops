# This puppet manifest to fix open file limits.

# Set the soft open file limit for the holberton user
exec { 'soft':
    command => '/bin/sed -i "s/holberton soft nofile 4/holberton soft nofile 1500/" /etc/security/limits.conf',
}

# Set the hard open file limit for the holberton user
exec { 'hard':
    command => '/bin/sed -i "s/holberton hard nofile 5/holberton hard nofile 1500/" /etc/security/limits.conf',
}

# Reload system settings to apply the changes
exec {'reload':
  command => '/usr/sbin/sysctl -p',
}

