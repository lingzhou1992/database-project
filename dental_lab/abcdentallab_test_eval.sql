SELECT * FROM restock_supply;
SELECT * FROM restock_material;

SELECT * FROM dental_office_balance;
SELECT * FROM technician_case_view;
SELECT * FROM driver_case_view;

CALL monthly_balance_sheet(2,2020);
CALL office_statement_by_date(1001,"2020-01-15","2020-02-12");
CALL get_case_info(10000);

INSERT INTO CASE_INVOICE_LINE VALUES(10261,114,'Framework with Teeth One Time Finish Upper and Lower',2.00,NULL,NULL,NULL);
SELECT * FROM CASE_INVOICE_LINE WHERE DEN_CASE_ID = 1026 AND SERVICE_CODE = 114;

INSERT INTO VEND_SUPPLY_LINE VALUES(8026,710033,3,12.33,NULL,NULL);
SELECT * FROM VEND_SUPPLY_LINE WHERE VINV_CODE = 8026 AND SUPPLY_ID = 710033;

INSERT INTO VEND_MATERIAL_LINE VALUES(8016,330,5,14.23,NULL,NULL);
SELECT * FROM VEND_MATERIAL_LINE WHERE VINV_CODE = 8016 AND MATERIAL_ID = 330;

CREATE USER 'officeManager'@'localhost' IDENTIFIED BY 'manager123@';
CREATE USER 'administrator'@'localhost' IDENTIFIED BY 'admin456!';
CREATE USER 'technician'@'localhost' IDENTIFIED BY 'tech789@';
CREATE USER 'driver'@'localhost' IDENTIFIED BY 'driver246&';
CREATE USER 'officeAssistant'@'localhost' IDENTIFIED BY 'office357&';

GRANT ALL ON *.* TO 'officeManager'@'localhost';
GRANT SELECT, INSERT, UPDATE, ALTER, DELETE, CREATE, DROP, CREATE VIEW, SHOW VIEW 
	ON abcdentallab.* TO 'administrator'@'localhost';
GRANT SELECT ON abcdentallab.* TO 'officeAssistant'@'localhost';
GRANT SELECT ON abcdentallab.technician_case_view TO 'technician'@'localhost';
GRANT SELECT ON abcdentallab.driver_case_view TO 'driver'@'localhost';

-- USER 'driver'@'localhost'
SELECT * FROM abcdentallab.office;
SELECT * FROM abcdentallab.driver_case_view;

-- USER 'technician'@'localhost'
UPDATE abcdentallab.technician_case_view set case_getdate = "2020-11-27" where case_id = 10285;
SELECT * FROM abcdentallab.technician_case_view;

-- USER 'officeAssistant'@'localhost'
ALTER TABLE abcdentallab.office DROP COLUMN office_hours;
SHOW DATABASES;
USE abcdentallab;
SELECT office_name from office where office_city = "Alameda";

-- USER 'officeManager'@'localhost'
DELETE FROM OCCUPATION WHERE OCCUPTAION_CODE = 602;
DELETE FROM OFFICE WHERE OFFICE_ID = 1001;
DELETE FROM SUPPLY WHERE SUPPLY_ID = 710001;
DELETE FROM MATERIAL WHERE MATERIAL_ID = 200;

ALTER TABLE OFFICE DROP COLUMN OFFICE_ID;
ALTER TABLE EMPLOYEE DROP COLUMN EMP_ID;
ALTER TABLE VENDOR DROP COLUMN VEND_ID;


UPDATE SERVICE SET SERVICE_PRICE = 1.10*SERVICE_PRICE WHERE SERVICE_CODE >= 112 AND SERVICE_CODE <= 128;
SELECT * FROM SERVICE;

UPDATE OCCUPATION SET OCCUPATION_SALARY=1.15*OCCUPATION_SALARY WHERE OCCUPATION_DESCRIPTION LIKE '%Manager' AND OCCUPATION_CODE <> 0;
UPDATE OCCUPATION SET OCCUPATION_SALARY=1.10*OCCUPATION_SALARY WHERE OCCUPATION_DESCRIPTION LIKE 'Technician%' AND OCCUPATION_CODE <> 0;
UPDATE OCCUPATION SET OCCUPATION_SALARY=1.08*OCCUPATION_SALARY WHERE OCCUPATION_DESCRIPTION LIKE 'Administrator%' AND OCCUPATION_CODE <> 0;
UPDATE OCCUPATION SET OCCUPATION_SALARY=1.05*OCCUPATION_SALARY WHERE OCCUPATION_DESCRIPTION LIKE 'Office Assistant%' AND OCCUPATION_CODE <> 0;
UPDATE OCCUPATION SET OCCUPATION_SALARY=1.03*OCCUPATION_SALARY WHERE OCCUPATION_DESCRIPTION LIKE 'Driver%' AND OCCUPATION_CODE <> 0;

SELECT * FROM OCCUPATION;

-- shell > mysqldump -u officeManager -p --single-transaction --flush-logs --master-data=2 --database abcdentallab > abcdentallab_backup.sql
-- shell > mysql -u officeManager -p abcdentallab > abcdentallab_backup.sql
