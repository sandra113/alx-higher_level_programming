-- this script creates MySQL server user
CREAT DATABASE IF NOT EXIST 'hbtn_0d_2'
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT ALL PRIVILEGES on *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
