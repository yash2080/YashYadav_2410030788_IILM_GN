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
EXPERIMENT -- 6
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
Date Functions and Formatting Queries
```{=html}
</h4>
```
```{=html}
</center>
```

------------------------------------------------------------------------

## Aim

To perform operations using date functions and formatting queries in
MariaDB.

------------------------------------------------------------------------

## Software Used

-   MariaDB / MySQL
-   Visual Studio Code

------------------------------------------------------------------------

## Queries

### 1. Display empno, ename and department name instead of department number (Decode equivalent)

``` sql
SELECT E.EMPNO, E.ENAME, D.DNAME
FROM EMPLOYEE E
JOIN DEPARTMENT D ON E.DEPTNO = D.DEPTNO;
```

------------------------------------------------------------------------

### 2. Display your age in days

``` sql
SELECT DATEDIFF(CURDATE(),'2003-01-01') AS AGE_IN_DAYS;
```

------------------------------------------------------------------------

### 3. Display your age in months

``` sql
SELECT TIMESTAMPDIFF(MONTH,'2003-01-01',CURDATE()) AS AGE_IN_MONTHS;
```

------------------------------------------------------------------------

### 4. Display current date as: 15th August Friday Nineteen Ninety-Seven (formatted date)

``` sql
SELECT DATE_FORMAT(NOW(),'%D %M %W %Y') AS FORMATTED_DATE;
```

------------------------------------------------------------------------

### 5. Display employee joining statement

``` sql
SELECT CONCAT(ENAME,' has joined the company on ',
DATE_FORMAT(HIREDATE,'%W %D %M %Y')) AS JOIN_INFO
FROM EMPLOYEE;
```

------------------------------------------------------------------------

### 6. Find the date for nearest Saturday after current date

``` sql
SELECT DATE_ADD(CURDATE(),
INTERVAL (7 - DAYOFWEEK(CURDATE()) + 7) % 7 DAY) AS NEXT_SATURDAY;
```

------------------------------------------------------------------------

### 7. Display current time

``` sql
SELECT CURRENT_TIME() AS CURRENT_TIME;
```

------------------------------------------------------------------------

### 8. Display the date three months before current date

``` sql
SELECT DATE_SUB(CURDATE(), INTERVAL 3 MONTH) AS THREE_MONTHS_BEFORE;
```

------------------------------------------------------------------------

### 9. Display employees who joined in the month of December

``` sql
SELECT ENAME, HIREDATE
FROM EMPLOYEE
WHERE MONTH(HIREDATE) = 12;
```

------------------------------------------------------------------------

### 10. Display employees whose first 2 characters of hire date equal last 2 characters of salary

``` sql
SELECT ENAME, HIREDATE, SAL
FROM EMPLOYEE
WHERE RIGHT(YEAR(HIREDATE),2) = RIGHT(SAL,2);
```

------------------------------------------------------------------------

### 11. Display employees whose 10% salary equals year of joining

``` sql
SELECT ENAME, SAL, HIREDATE
FROM EMPLOYEE
WHERE ROUND(SAL*0.10) = YEAR(HIREDATE);
```

------------------------------------------------------------------------

### 12. Display employees who joined before the 15th of the month

``` sql
SELECT ENAME, HIREDATE
FROM EMPLOYEE
WHERE DAY(HIREDATE) < 15;
```

------------------------------------------------------------------------

### 13. Display employees who joined on the 15th of the month

``` sql
SELECT ENAME, HIREDATE
FROM EMPLOYEE
WHERE DAY(HIREDATE) = 15;
```

------------------------------------------------------------------------

### 14. Display employees whose joining date day equals department number

``` sql
SELECT ENAME, HIREDATE, DEPTNO
FROM EMPLOYEE
WHERE DAY(HIREDATE) = DEPTNO;
```

------------------------------------------------------------------------

### 15. Display employees whose joining DATE value exists as department number

``` sql
SELECT ENAME, HIREDATE, DEPTNO
FROM EMPLOYEE
WHERE DAY(HIREDATE) IN (SELECT DEPTNO FROM DEPARTMENT);
```

------------------------------------------------------------------------

## Result

All date and formatting related SQL queries were successfully executed
using MariaDB.
