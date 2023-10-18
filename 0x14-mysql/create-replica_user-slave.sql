-- Create 'replica_user' with host '%' and set a password (change 'your_replica_user_password' to your desired password)
CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'slave@123';

-- Grant replication permissions to 'replica_user'
GRANT REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'replica_user'@'%';

-- Grant SELECT privileges on the 'mysql.user' table to 'holberton_user'
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';

-- Apply the changes
FLUSH PRIVILEGES;
