CREATE TABLE Employee (
    empID Integer NOT NULL,
    empName char(25) NOT NULL,
    salaryCode Integer,
    deptID Integer,
    phone char(25),
    CONSTRAINT empPk PRIMARY KEY(empID)
);

CREATE TABLE Skill (
    skillID INTEGER NOT NULL,
    CONSTRAINT skillpk PRIMARY KEY(skillID)
);

CREATE TABLE EmployeeSkill (
    empID Integer NOT NULL,
    skillID Integer NOT NULL,
    skillLevel Integer NULL,
    CONSTRAINT empSkillPK PRIMARY KEY(empID, skillID),
    CONSTRAINT empFk FOREIGN KEY(empID) REFERENCES Employee(EmpId) ON DELETE CASCADE,
    CONSTRAINT empSkill FOREIGN KEY(skillID) REFERENCES Skill(skillID) ON DELETE CASCADE
);

ALTER TABLE Employee
    ADD CONSTRAINT empPk PRIMARY KEY(empId);
    
ALTER TABLE EmployeeSkill
    ADD CONSTRAINT empSkillPK
        PRIMARY KEY(empId, skillId);
        
INSERT INTO Employee (empId, empName)
    VALUES (62, 'Halpert');
    
UPDATE Employee
SET phone = '515-162-1551'
WHERE empName = 'Halpert';

UPDATE Employee
SET deptID = 4
WHERE empName LIKE 'Da%'

UPDATE Employee
SET deptID = 3;

DELETE FROM Employee
WHERE empId = 29;

DELETE FROM Employee
WHERE empName LIKE 'Da%';

-- DELETE FROM Employee;

SELECT empName
FROM Employee
WHERE empId = 62;

SELECT empID, empName
FROM Employee;
--Select all columns from Employee table
SELECT * 
FROM Employee;

SELECT empName
FROM Employee
WHERE deptID < 7 OR deptID > 12

SELECT empName
FROM Employee
WHERE deptID = 9 AND salaryCode > 1000

SELECT empName
FROM Employee
WHERE deptId IN (4, 8, 9);
-- WHERE deptID = 4 OR deptID = 8 OR deptID = 9

SELECT empName
FROM Employee
WHERE deptId NOT IN (4, 8, 9)
-- A l ist of employee names in the table for all deptIDs other than 4, 8, 9

--Between allows any values in that range is accecptable
SELECT empName
FROM Employee
WHERE salaryCode BETWEEN 10 AND 45
--COMPARE to WHERE

--Like keyword can be paired with wildcards to find rows that partially match a string values;
--The multiple character wildcard character is a percent sign%;
--The single character wildcard character is an underscore;

 


