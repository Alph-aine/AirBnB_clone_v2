-- MySQL test server for this project
CREATE DATABASE IF NOT EXISTS hbnd_test_db;
CREATE USER IF NOT EXISTS 'hbn_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnd_test_db . * TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema . * TO 'hbnb_test'@'localhost';

