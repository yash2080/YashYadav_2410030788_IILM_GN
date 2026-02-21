```{=html}
<center>
```
```{=html}
<h2>
```
DATABASE MANAGEMENT SYSTEM LAB
```{=html}
</h2>
```
```{=html}
</center>
```
```{=html}
<center>
```
```{=html}
<h3>
```
EXPERIMENT -- 5
```{=html}
</h3>
```
```{=html}
</center>
```
`<br>`{=html}

```{=html}
<center>
```
```{=html}
<h4>
```
Aggregate Functions and String Functions in SQL
```{=html}
</h4>
```
```{=html}
</center>
```

------------------------------------------------------------------------

## Aim

To perform aggregate operations and string manipulations using SQL
functions in MariaDB.

------------------------------------------------------------------------

## Software Used

-   MariaDB / MySQL
-   Visual Studio Code

------------------------------------------------------------------------

## Queries

### 1. Display the total number of employees working in the company

``` sql
SELECT COUNT(*) AS TOTAL_EMPLOYEES
FROM EMPLOYEE;
```

------------------------------------------------------------------------

### 2. Display the total salary being paid to all employees

``` sql
SELECT SUM(SAL) AS TOTAL_SALARY
FROM EMPLOYEE;
```

------------------------------------------------------------------------

### 3. Display the maximum salary from employee table

``` sql
SELECT MAX(SAL) AS MAX_SALARY
FROM EMPLOYEE;
```

------------------------------------------------------------------------

### 4. Display the minimum salary from employee table

``` sql
SELECT MIN(SAL) AS MIN_SALARY
FROM EMPLOYEE;
```

------------------------------------------------------------------------

### 5. Display the average salary from employee table

``` sql
SELECT AVG(SAL) AS AVG_SALARY
FROM EMPLOYEE;
```

------------------------------------------------------------------------

### 6. Display the maximum salary being paid to clerk

``` sql
SELECT MAX(SAL) AS MAX_CLERK_SALARY
FROM EMPLOYEE
WHERE JOB = 'CLERK';
```

------------------------------------------------------------------------

### 7. Display the maximum salary being paid in department number 20

``` sql
SELECT MAX(SAL) AS MAX_DEPT20_SALARY
FROM EMPLOYEE
WHERE DEPTNO = 20;
```

------------------------------------------------------------------------

### 8. Display the minimum salary paid to any salesman

``` sql
SELECT MIN(SAL) AS MIN_SALESMAN_SALARY
FROM EMPLOYEE
WHERE JOB = 'SALESMAN';
```

------------------------------------------------------------------------

### 9. Display the average salary drawn by managers

``` sql
SELECT AVG(SAL) AS AVG_MANAGER_SALARY
FROM EMPLOYEE
WHERE JOB = 'MANAGER';
```

------------------------------------------------------------------------

### 10. Display the total salary drawn by analysts working in department 40

``` sql
SELECT SUM(SAL) AS TOTAL_ANALYST_DEPT40
FROM EMPLOYEE
WHERE JOB = 'ANALYST'
AND DEPTNO = 40;
```

------------------------------------------------------------------------

### 11. Display employee names in uppercase

``` sql
SELECT UPPER(ENAME) AS UPPERCASE_NAME
FROM EMPLOYEE;
```

------------------------------------------------------------------------

### 12. Display employee names in lowercase

``` sql
SELECT LOWER(ENAME) AS LOWERCASE_NAME
FROM EMPLOYEE;
```

------------------------------------------------------------------------

### 13. Display employee names in proper case

``` sql
SELECT CONCAT(UPPER(LEFT(ENAME,1)), LOWER(SUBSTRING(ENAME,2))) AS PROPER_NAME
FROM EMPLOYEE;
```

------------------------------------------------------------------------

### 14. Display the length of your name (example)

``` sql
SELECT LENGTH('SAHIL') AS NAME_LENGTH;
```

------------------------------------------------------------------------

### 15. Display the length of all employee names

``` sql
SELECT ENAME, LENGTH(ENAME) AS NAME_LENGTH
FROM EMPLOYEE;
```

------------------------------------------------------------------------

## Result

Aggregate and string functions were successfully executed using MariaDB
SQL queries.
