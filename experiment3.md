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
EXPERIMENT -- 3
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
Data Retrieval Using ORDER BY, LIKE and Conditional Queries
```{=html}
</h4>
```
```{=html}
</center>
```

------------------------------------------------------------------------

## Aim

To perform data retrieval using ORDER BY clause, pattern matching and
conditional SQL queries in MariaDB.

------------------------------------------------------------------------

## Software Used

-   MariaDB / MySQL
-   Visual Studio Code

------------------------------------------------------------------------

## Queries

### 1. List all employees and jobs in Department 30 in descending order by salary

``` sql
SELECT ENAME, JOB, SAL
FROM EMPLOYEE
WHERE DEPTNO = 30
ORDER BY SAL DESC;
```

------------------------------------------------------------------------

### 2. List job and department number of employees whose name has five letters, begins with 'A' and ends with 'N'

``` sql
SELECT JOB, DEPTNO
FROM EMPLOYEE
WHERE ENAME LIKE 'A___N';
```

------------------------------------------------------------------------

### 3. Display the names of employees whose name starts with alphabet S

``` sql
SELECT ENAME
FROM EMPLOYEE
WHERE ENAME LIKE 'S%';
```

------------------------------------------------------------------------

### 4. Display the names of employees whose name ends with alphabet S

``` sql
SELECT ENAME
FROM EMPLOYEE
WHERE ENAME LIKE '%S';
```

------------------------------------------------------------------------

### 5. Display employees working in department 10, 20 or 40 or working as clerk, salesman or analyst

``` sql
SELECT *
FROM EMPLOYEE
WHERE DEPTNO IN (10,20,40)
OR JOB IN ('CLERK','SALESMAN','ANALYST');
```

------------------------------------------------------------------------

### 6. Display employee number and names for employees who earn commission

``` sql
SELECT EMPNO, ENAME
FROM EMPLOYEE
WHERE COMM IS NOT NULL
AND COMM > 0;
```

------------------------------------------------------------------------

### 7. Display employee number and total salary for each employee

``` sql
SELECT EMPNO, (SAL + IFNULL(COMM,0)) AS TOTAL_SALARY
FROM EMPLOYEE;
```

------------------------------------------------------------------------

### 8. Display employee number and annual salary for each employee

``` sql
SELECT EMPNO, (SAL * 12) AS ANNUAL_SALARY
FROM EMPLOYEE;
```

------------------------------------------------------------------------

### 9. Display names of employees working as clerks and drawing salary more than 3000

``` sql
SELECT ENAME
FROM EMPLOYEE
WHERE JOB = 'CLERK'
AND SAL > 3000;
```

------------------------------------------------------------------------

### 10. Display names of employees working as clerk, salesman or analyst and drawing salary more than 3000

``` sql
SELECT ENAME
FROM EMPLOYEE
WHERE JOB IN ('CLERK','SALESMAN','ANALYST')
AND SAL > 3000;
```

------------------------------------------------------------------------

## Result

The required SQL queries using ORDER BY, LIKE and conditional clauses
were successfully executed in MariaDB.
