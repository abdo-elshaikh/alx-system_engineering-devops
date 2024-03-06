# Puppet manifest to fix Apache 500 error
# Ensure Apache service is running
service { 'apache2':
  ensure => running,
}

exec { 'Fix wordpress site':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}
