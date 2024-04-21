-- A script that prepares a MySQL server for the project:
-- A database hbnb_dev_db
-- A new user hbnb_dev (in localhost)
-- The password of hbnb_dev should be set to hbnb_dev_pwd

-- Create database hbnb_dev_db if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create user hbnb_dev if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on hbnb_dev_db to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on performance_schema to hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
