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
EXPERIMENT -- 4
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
Data Manipulation Using Date, String and Arithmetic Functions
```{=html}
</h4>
```
```{=html}
</center>
```

------------------------------------------------------------------------

## Aim

To perform data manipulation using date functions, string functions and
arithmetic operations in MariaDB.

------------------------------------------------------------------------

## Software Used

-   MariaDB / MySQL
-   Visual Studio Code

------------------------------------------------------------------------

## Queries

### 1. Display employees who joined before 30-June-1980 or after 31-Dec-1981

``` sql
SELECT ENAME, HIREDATE
FROM EMPLOYEE
WHERE HIREDATE < '1980-06-30'
OR HIREDATE > '1981-12-31';
```

------------------------------------------------------------------------

### 2. Display names of employees whose second letter is 'A'

``` sql
SELECT ENAME
FROM EMPLOYEE
WHERE ENAME LIKE '_A%';
```

------------------------------------------------------------------------

### 3. Display names of employees whose names are exactly five characters long

``` sql
SELECT ENAME
FROM EMPLOYEE
WHERE LENGTH(ENAME) = 5;
```

------------------------------------------------------------------------

### 4. Display names of employees whose second letter is 'A'

``` sql
SELECT ENAME
FROM EMPLOYEE
WHERE ENAME LIKE '_A%';
```

------------------------------------------------------------------------

### 5. Display names of employees who are not working as salesman, clerk or analyst

``` sql
SELECT ENAME, JOB
FROM EMPLOYEE
WHERE JOB NOT IN ('SALESMAN','CLERK','ANALYST');
```

------------------------------------------------------------------------

### 6. Display employee name along with annual salary (highest salary first)

``` sql
SELECT ENAME, (SAL * 12) AS ANNUAL_SALARY
FROM EMPLOYEE
ORDER BY ANNUAL_SALARY DESC;
```

------------------------------------------------------------------------

### 7. Display name, salary, HRA (15%), DA (10%), PF (5%) and total salary

``` sql
SELECT 
ENAME,
SAL,
SAL * 0.15 AS HRA,
SAL * 0.10 AS DA,
SAL * 0.05 AS PF,
(SAL + (SAL*0.15) + (SAL*0.10) - (SAL*0.05)) AS TOTALSAL
FROM EMPLOYEE
ORDER BY TOTALSAL;
```

------------------------------------------------------------------------

### 8. Update salary by 10% increment for employees not eligible for commission

``` sql
UPDATE EMPLOYEE
SET SAL = SAL * 1.10
WHERE COMM IS NULL;
```

------------------------------------------------------------------------

### 9. Display employees whose salary becomes greater than 3000 after 20% increment

``` sql
SELECT ENAME, SAL * 1.20 AS NEW_SALARY
FROM EMPLOYEE
WHERE SAL * 1.20 > 3000;
```

------------------------------------------------------------------------

### 10. Display employees whose salary contains at least three digits

``` sql
SELECT ENAME, SAL
FROM EMPLOYEE
WHERE SAL >= 100;
```

------------------------------------------------------------------------

## Result

The required SQL queries using date functions, string operations and
arithmetic calculations were successfully executed in MariaDB.
