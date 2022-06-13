USE mysql;
UPDATE user SET authentication_string=PASSWORD('P@$$w0rd') WHERE User='root';
FLUSH PRIVILEGES;