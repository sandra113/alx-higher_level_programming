-- prints the full description of the table first_table
SELECT
    table_name AS 'Table',
    CONCAT('CREATE TABLE `', table_name, '` (') AS 'Create Table'
FROM information_schema.tables
WHERE table_schema = 'hbtn_0c_0'
AND table_name = 'first_table';

SELECT
    GROUP_CONCAT(
        CONCAT('  `', column_name, '` ', column_type, ' ',
        IF(column_default IS NOT NULL, 'DEFAULT ' + column_default, ''), ',')
    ) AS 'Create Table'
FROM information_schema.columns
WHERE table_name = 'first_table' AND table_schema = 'hbtn_0c_0'
GROUP BY table_name;

