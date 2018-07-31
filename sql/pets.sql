DROP DATABASE IF EXISTS pets;
CREATE DATABASE IF NOT EXISTS pets;
USE pets;

SELECT 'Creating tables...' as 'INFO';

CREATE TABLE pets (
  ID INT NOT NULL AUTO_INCREMENT,
  account_num INT NOT NULL,
  name VARCHAR(50) NOT NULL,
  animal_type VARCHAR(25) NOT NULL,
  gender ENUM('M', 'F')  NOT NULL,
  birthdate DATE NOT NULL,
  owner_firstname VARCHAR(25),
  owner_lastname VARCHAR(25),
  owner_phone BIGINT,
  PRIMARY KEY (ID)
);

CREATE TABLE visits (
  ID INT NOT NULL AUTO_INCREMENT,
  account_num INT NOT NULL,
  visit_date DATE NOT NULL,
  reason TEXT NOT NULL,
  PRIMARY KEY (ID)
);
SELECT 'Done!' as 'INFO';
SELECT 'LOADING pets with data...' as 'INFO';
source pets.dump;
SELECT 'LOADING visits with data...' as 'INFO';
source visits.dump;

SELECT count(*) as 'Rows inserted into pets:' from pets;
SELECT count(*) as 'Rows inserted into visits:' from visits;