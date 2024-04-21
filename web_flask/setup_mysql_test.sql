-- SQL script that prepares a MySQL server for the project:
-- A database hbnb_test_db
-- A new user hbnb_test (in localhost)
-- The password of hbnb_test should be set to hbnb_test_pwd

-- Create database hbnb_test_db if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create user hbnb_test if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on hbnb_test_db to hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on performance_schema to hbnb_test
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
