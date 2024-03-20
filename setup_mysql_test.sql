-- creates a database hbnb_test_db
CREATE IF NOT EXISTS DATABASE hbnb_test_db;
-- create a new user hbnb_test in localhost
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grant all privileges on the database hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
-- grant select privileges on the database performance schema
GRANT SELECT PRIVILEGES ON performance_schema.* ON 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;

