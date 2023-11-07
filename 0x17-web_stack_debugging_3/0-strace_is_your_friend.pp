# Using strace, find out why Apache is returning a 500 error.

exec { 'no phpp':
    command => '/bin/sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php'
}
exec {'restart web server':
  command => '/usr/sbin/service apache2 restart'
}
