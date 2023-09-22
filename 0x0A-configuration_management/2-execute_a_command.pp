# This puppet Manifest for killing 
# A process named "killmenow" using pkill

exec { 'killmenow':
  command => '/usr/bin/pkill --full killmenow',
}

