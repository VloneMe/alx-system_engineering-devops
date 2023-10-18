-- Create the 'tyrell_corp' database if it doesn't exist
CREATE DATABASE IF NOT EXISTS tyrell_corp;

-- Use the 'tyrell_corp' database
USE tyrell_corp;

-- Create the 'nexus6' table if it doesn't exist
CREATE TABLE IF NOT EXISTS nexus6 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    model VARCHAR(255)
);

-- Insert a sample entry into the 'nexus6' table
INSERT INTO nexus6 (name, model) VALUES ('Sample Nexus 6', 'Model XYZ');

-- Grant SELECT permissions to the 'holberton_user' on the 'nexus6' table
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';

-- Flush privileges to apply the changes
FLUSH PRIVILEGES;
