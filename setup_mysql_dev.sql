-- Creates a MYSQL server with
-- Database hbnb_dev_db
-- User hbnb_dev in localhost witb password hbnb_test_pwd
-- Grants all priviliges for hbnb_test on hbnb_test_db
-- Grants SELECT priviliges hbnb_test on performance_schema

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
FLUSH PRIVILEGES;
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
