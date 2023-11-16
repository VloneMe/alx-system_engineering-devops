# This puppet manifest fixs nginx worker processes.

exec { 'worker action':
    command => '/bin/sed -i "s/15/1500/g" /etc/default/nginx'
}
-> exec {'restart server':
  command => '/usr/sbin/service nginx restart'
}
