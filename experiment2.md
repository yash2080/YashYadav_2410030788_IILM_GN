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
EXPERIMENT -- 2
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
Retrieving Data Using SQL Queries
```{=html}
</h4>
```
```{=html}
</center>
```

------------------------------------------------------------------------

## Aim

To retrieve data from database tables using various SQL SELECT queries
in MariaDB.

------------------------------------------------------------------------

## Software Used

-   MariaDB / MySQL
-   Visual Studio Code

------------------------------------------------------------------------

## Queries

### 1. List all distinct jobs in Employee

``` sql
SELECT DISTINCT JOB
FROM EMPLOYEE;
```

------------------------------------------------------------------------

### 2. List all information about employees in Department Number 30

``` sql
SELECT *
FROM EMPLOYEE
WHERE DEPTNO = 30;
```

------------------------------------------------------------------------

### 3. Find all department numbers with department names greater than 20

``` sql
SELECT *
FROM DEPARTMENT
WHERE DEPTNO > 20;
```

------------------------------------------------------------------------

### 4. Find all managers as well as clerks in department 30

``` sql
SELECT *
FROM EMPLOYEE
WHERE DEPTNO = 30
AND JOB IN ('MANAGER','CLERK');
```

------------------------------------------------------------------------

### 5. List employee name, employee number and department of all clerks

``` sql
SELECT ENAME, EMPNO, DEPTNO
FROM EMPLOYEE
WHERE JOB = 'CLERK';
```

------------------------------------------------------------------------

### 6. Find all managers not in department 30

``` sql
SELECT *
FROM EMPLOYEE
WHERE JOB = 'MANAGER'
AND DEPTNO <> 30;
```

------------------------------------------------------------------------

### 7. List information about employees in department 10 who are not managers or clerks

``` sql
SELECT *
FROM EMPLOYEE
WHERE DEPTNO = 10
AND JOB NOT IN ('MANAGER','CLERK');
```

------------------------------------------------------------------------

### 8. Find employees and jobs earning between 1200 and 1400

``` sql
SELECT ENAME, JOB
FROM EMPLOYEE
WHERE SAL BETWEEN 1200 AND 1400;
```

------------------------------------------------------------------------

### 9. List name and department number of employees who are clerks, analysts or salesman

``` sql
SELECT ENAME, DEPTNO
FROM EMPLOYEE
WHERE JOB IN ('CLERK','ANALYST','SALESMAN');
```

------------------------------------------------------------------------

### 10. List name and department number of employees whose names begin with M

``` sql
SELECT ENAME, DEPTNO
FROM EMPLOYEE
WHERE ENAME LIKE 'M%';
```

------------------------------------------------------------------------

## Result

The required data retrieval operations were successfully performed using
SQL SELECT queries in MariaDB.
