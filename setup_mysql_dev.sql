-- MySQL test server for this project
CREATE DATABASE IF NOT EXISTS hbnd_dev_db;
CREATE USER IF NOT EXISTS 'hbn_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnd_dev_db . * TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema . * TO 'hbnb_dev'@'localhost';

