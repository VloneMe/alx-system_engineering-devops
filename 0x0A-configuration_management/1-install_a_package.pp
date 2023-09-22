# This puppet Manifest for installing Flask via pip3

# This defines a package resource to install Flask
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
