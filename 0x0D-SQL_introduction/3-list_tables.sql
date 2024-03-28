-- List the tables of a database in mysql

USE mysql;
SELECT *
FROM information_schema.tables
WHERE table_schema = 'mysql';
