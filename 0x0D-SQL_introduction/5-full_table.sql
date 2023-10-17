-- prints the full description of the table first_table
SELECT *FROM information_schema.columns
WHERE table_name = 'first_table' AND table_schema = 'hbtn_0c_0';
