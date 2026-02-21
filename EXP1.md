# DATABASE MANAGEMENT SYSTEM LAB

## Practical File -- MariaDB SQL Experiments

**Student Name:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\
**Roll No:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\
**Date:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\
**Database Used:** MariaDB / MySQL

------------------------------------------------------------------------

# Experiment 1: Table Creation and Data Insertion

## Aim:

To create EMPLOYEE and DEPARTMENT tables and insert records.

## SQL Queries:

### Create DEPARTMENT Table

``` sql
CREATE TABLE DEPARTMENT (
    DEPTNO INT PRIMARY KEY,
    DNAME VARCHAR(15) NOT NULL
);
```

### Insert into DEPARTMENT

``` sql
INSERT INTO DEPARTMENT VALUES (10,'RESEARCH');
INSERT INTO DEPARTMENT VALUES (20,'ACCOUNTING');
INSERT INTO DEPARTMENT VALUES (30,'SALES');
INSERT INTO DEPARTMENT VALUES (40,'OPERATIONS');
```

### Create EMPLOYEE Table

``` sql
CREATE TABLE EMPLOYEE (
    EMPNO INT PRIMARY KEY,
    ENAME VARCHAR(20) NOT NULL,
    JOB VARCHAR(20),
    MGR INT,
    HIREDATE DATE,
    SAL DECIMAL(10,2),
    COMM DECIMAL(10,2),
    DEPTNO INT,
    FOREIGN KEY (DEPTNO) REFERENCES DEPARTMENT(DEPTNO)
);
```

------------------------------------------------------------------------

# Experiment 2: Basic Retrieval Queries

## Aim:

To perform basic SELECT operations.

``` sql
SELECT DISTINCT JOB FROM EMPLOYEE;

SELECT * FROM EMPLOYEE WHERE DEPTNO = 30;

SELECT DEPTNO, DNAME FROM DEPARTMENT WHERE DEPTNO > 20;

SELECT ENAME, EMPNO, DEPTNO FROM EMPLOYEE WHERE JOB='CLERK';

SELECT ENAME, DEPTNO FROM EMPLOYEE WHERE ENAME LIKE 'M%';
```

------------------------------------------------------------------------

# Experiment 3: Conditions and Sorting

## Aim:

To apply conditions, pattern matching and ordering.

``` sql
SELECT ENAME, JOB, SAL FROM EMPLOYEE 
WHERE DEPTNO=30 ORDER BY SAL DESC;

SELECT JOB, DEPTNO FROM EMPLOYEE 
WHERE ENAME LIKE 'A___N';

SELECT ENAME FROM EMPLOYEE WHERE ENAME LIKE 'S%';

SELECT ENAME FROM EMPLOYEE WHERE ENAME LIKE '%S';
```

------------------------------------------------------------------------

# Experiment 4: Aggregate Functions

## Aim:

To use aggregate functions.

``` sql
SELECT COUNT(*) FROM EMPLOYEE;
SELECT SUM(SAL) FROM EMPLOYEE;
SELECT MAX(SAL) FROM EMPLOYEE;
SELECT MIN(SAL) FROM EMPLOYEE;
SELECT AVG(SAL) FROM EMPLOYEE;
```

------------------------------------------------------------------------

# Experiment 5: String Functions

## Aim:

To use string functions.

``` sql
SELECT UPPER(ENAME) FROM EMPLOYEE;
SELECT LOWER(ENAME) FROM EMPLOYEE;
SELECT CONCAT(UPPER(LEFT(ENAME,1)), LOWER(SUBSTRING(ENAME,2))) FROM EMPLOYEE;
SELECT ENAME, LENGTH(ENAME) FROM EMPLOYEE;
```

------------------------------------------------------------------------

# Experiment 6: Date Functions (MariaDB)

## Aim:

To perform date-based queries.

### Display empno, ename and department name using CASE

``` sql
SELECT EMPNO,
       ENAME,
       CASE 
           WHEN DEPTNO=10 THEN 'RESEARCH'
           WHEN DEPTNO=20 THEN 'ACCOUNTING'
           WHEN DEPTNO=30 THEN 'SALES'
           WHEN DEPTNO=40 THEN 'OPERATIONS'
           ELSE 'UNKNOWN'
       END AS DEPARTMENT_NAME
FROM EMPLOYEE;
```

### Age in Days

``` sql
SELECT DATEDIFF(CURDATE(),'2005-01-15') AS AGE_IN_DAYS;
```

### Age in Months

``` sql
SELECT TIMESTAMPDIFF(MONTH,'2005-01-15',CURDATE()) AS AGE_IN_MONTHS;
```

### Current Date Format

``` sql
SELECT DATE_FORMAT(CURDATE(),'%D %M %W %Y');
```

### Message for Each Employee

``` sql
SELECT CONCAT(ENAME,' has joined the company on ',
DATE_FORMAT(HIREDATE,'%W %D %M %Y')) AS MESSAGE
FROM EMPLOYEE;
```

### Current Time

``` sql
SELECT CURTIME();
```

------------------------------------------------------------------------