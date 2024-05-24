SELECT 
    d1.name AS Department, 
    e1.name AS Employee, 
    e1.salary AS Salary
FROM 
    Employee e1
JOIN 
    Department d1 ON e1.departmentId = d1.id
WHERE 
    (
        SELECT COUNT(DISTINCT e2.salary) 
        FROM Employee e2 
        WHERE e2.salary > e1.salary AND e2.departmentId = e1.departmentId
    ) < 3;

-- mor optimized but less readable
/* Write your PL/SQL query statement below */
WITH RankedSalaries AS (
    SELECT
        e.name AS Employee,
        e.salary AS Salary,
        d.name AS Department,
        DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS SalaryRank
    FROM
        Employee e
    JOIN
        Department d ON e.departmentId = d.id
)
SELECT
    Department,
    Employee,
    Salary
FROM
    RankedSalaries
WHERE
    SalaryRank <= 3;