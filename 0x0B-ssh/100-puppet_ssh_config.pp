# This modify SSH client configuration to refuse password 
# authentication and specify an identity file.

exec { 'change_ssh_config':
  command  => 'echo "PasswordAuthentication no\nIdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
  provider => 'shell'
}

