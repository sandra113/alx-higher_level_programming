-- This script creates the table force_name
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

-- Switch to the 'hbtn_0d_usa' database
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities
(
	id INT AUTO_INCREMENT PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCE states(id)
);
