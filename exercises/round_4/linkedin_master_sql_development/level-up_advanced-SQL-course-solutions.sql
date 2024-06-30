/*
Solutions to challenges from:

Level Up: Advanced SQL
COURSE Course

    LinkedIn
    By: Jess Pomfret
    Mar 2023

*/

/*
1. Challenge
Retrieve a list of employers, including first and last names, and the first and last names of their immediate managers
Employee table, needs selfjoin or subquery
*/

SELECT e.firstName, 
  e.lastName,
  em.firstName AS manager_firstName,
  em.lastName AS manager_lastName
FROM employee AS e
INNER JOIN employee AS em
  ON e.employeeId = em.managerId
ORDER BY e.firstName

-- Subquery approach
SELECT e.firstName, 
  e.lastName,
  (
    SELECT firstName 
    FROM employee
    WHERE employeeId = e.managerId
  ) AS manager_firstName,
  (
    SELECT lastName 
    FROM employee
    WHERE employeeId = e.managerId
  ) AS manager_lastName
FROM employee as e
ORDER BY e.firstName



/*
2. Challenge
Get a list of salespeople with zero sales
*/
SELECT e.firstName,
  e.lastName
FROM employee AS e
LEFT JOIN sales AS s
  ON e.employeeId = s.employeeId
WHERE e.title = 'Sales Person' AND s.employeeId IS NULL;



/*
3. Challenge
List all sales and all customers even if some of the data has been removed.
*/
SELECT * 
FROM employee AS e
FULL OUTER JOIN sales AS s
  ON e.employeeId = s.employeeId
WHERE e.title = 'Sales Person'



/*
4. Challenge
Pull a report that totals the number of cars sold by each employee.
*/
SELECT e.employeeId,
  e.firstName,
  e.lastName,
  COUNT(s.salesId) AS salesCount
FROM sales AS s
INNER JOIN employee AS e
  ON s.employeeId = e.employeeId
GROUP BY e.employeeId,firstName, lastName
ORDER BY COUNT(salesId) DESC;



/*
4. Challenge
Produce a report that lists the least and most expensive car sold by each employee this year.
*/
SELECT e.employeeId,
  e.firstName,
  e.lastName,
  MAX(s.salesAmount) AS topSale,
  MIN(s.salesAmount) AS bottomSale
FROM sales AS s
INNER JOIN employee AS e
  ON s.employeeId = e.employeeId
WHERE strftime('%Y', s.soldDate) = '2023'
GROUP by e.employeeId, e.firstName, e.lastName
ORDER BY MAX(s.salesAmount) DESC;



/*
5. Challenge
Get a list of employees who have made more than five sales this year.
*/
SELECT e.employeeId,
  e.firstName,
  e.lastName
FROM sales AS s
INNER JOIN employee AS e
  ON s.employeeId = e.employeeId
WHERE strftime('%Y', s.soldDate) = '2023'
GROUP BY e.employeeId, e.firstName, e.lastName
HAVING COUNT(s.soldDate) > 5
ORDER BY e.employeeId;



/*
6. Challenge
Use CTE and show report with total sales per year.
*/
-- Create CTE to have only year instead of date and amounts
WITH cte_salesYearly AS (
  SELECT 
    strftime('%Y', soldDate) AS salesYear,
    salesAmount
  FROM sales
)
SELECT 
  salesYear,
  ROUND(SUM(salesAmount),2) AS totalSales
FROM cte_salesYearly
GROUP BY salesYear
ORDER BY salesYear DESC;


/*
7. Challenge
Create a report displaying sales for each employee by month for 2021.
*/

-- Create CTE to have joined data set ready with correct date formats
-- Then use case statement to pivot data into monthly colums by conditioning the month value
-- Then wrap that in SUM() and ordred by employee so I get aggregated values
WITH cte_sales AS (
SELECT 
    e.employeeId,
    e.firstName,
    e.lastName,
    strftime('%Y', s.soldDate) AS salesYear,
    strftime('%m', s.soldDate) AS salesMonth,
    salesAmount
  FROM sales AS s
  INNER JOIN employee as e
  ON s.employeeId = e.employeeId
  WHERE strftime('%Y', s.soldDate) = '2021'
)

SELECT 
  firstName,
  lastName,
  SUM(CASE WHEN salesMonth = '01' THEN salesAmount END) AS salesJanuary,
  SUM(CASE WHEN salesMonth = '02' THEN salesAmount END) AS salesFebruary,
  SUM(CASE WHEN salesMonth = '03' THEN salesAmount END) AS salesMarch,
  SUM(CASE WHEN salesMonth = '04' THEN salesAmount END) AS salesApril,
  SUM(CASE WHEN salesMonth = '05' THEN salesAmount END) AS salesMay,
  SUM(CASE WHEN salesMonth = '06' THEN salesAmount END) AS salesJune,
  SUM(CASE WHEN salesMonth = '07' THEN salesAmount END) AS salesJuly,
  SUM(CASE WHEN salesMonth = '08' THEN salesAmount END) AS salesAugust,
  SUM(CASE WHEN salesMonth = '09' THEN salesAmount END) AS salesSeptember,
  SUM(CASE WHEN salesMonth = '10' THEN salesAmount END) AS salesOctober,
  SUM(CASE WHEN salesMonth = '11' THEN salesAmount END) AS salesNovember,
  SUM(CASE WHEN salesMonth = '12' THEN salesAmount END) AS salesDecember
FROM cte_sales
GROUP BY firstName, lastName
ORDER BY lastName, firstName;



/*
8. Challenge
Find all sales where the car purchased was electric.
Use subquery.
*/

-- Select everything from sales table
-- where id is found in inventory table in which 
-- the model id is found in model table for cars whose engine type is 'Electric'

SELECT * 
FROM sales AS s
WHERE s.inventoryId IN (
  SELECT inventoryId 
  FROM inventory AS i
  WHERE modelId IN (
    SELECT modelId 
    FROM model AS m
    WHERE EngineType = 'Electric'
  )
)



/*
9. Challenge
Get a list of sales people and rank the car models they've sold the most of.
*/

-- Get data from sales, employees and inventory tables with only needed columns
WITH cte_modelsSold AS (
SELECT 
  e.employeeId,
  e.firstName,
  e.lastName,
  m.model
FROM employee AS e
INNER JOIN sales AS s
  ON e.employeeId = s.employeeId
INNER JOIN inventory AS i 
  ON s.inventoryId = i.inventoryId
INNER JOIN model AS m
  ON i.modelId = m.modelId
)

-- First group data to count models
-- Then apply rank() windows function to rank sales per car
-- Trick is to order it by count of the model
SELECT 
  firstName,
  lastName,
  model,
  COUNT(model) AS numOfSales,
  DENSE_RANK() OVER (
    PARTITION BY employeeId
    ORDER BY COUNT(model) DESC
    ) AS salesRank
FROM cte_modelsSold
GROUP BY firstName, lastName, model



/*
10. Challenge
Generate sales report showing total sales per month and an annual running total.
*/

-- Select dates formatted as year and month
-- Select sum of amounts then group by year and month to get aggregated sales per month
-- Then do sum() as windows function partitioned by year and ordered by month to get the running totals
SELECT 
    strftime('%Y', soldDate) AS sYear,
    strftime('%m', soldDate) AS sMonth,
    sum(salesAmount) AS monthlySales,
    SUM(salesAmount) OVER(
      PARTITION BY strftime('%Y', soldDate)
      ORDER BY 
        strftime('%Y', soldDate), 
        strftime('%m', soldDate)
    ) as yearlyRunningTotal
FROM sales
GROUP BY sYear, sMonth;



/*
11. Challenge
Create a report showing number of cars sold this month and last month.
*/


SELECT 
  strftime('%Y', soldDate) AS year,
  strftime('%m', soldDate) AS month,
  count(salesId) AS numberOfSales
FROM sales
WHERE 
  -- This and last month won't work as the course do not have this year data (2024)
  -- strftime('%Y', soldDate) = strftime('%Y', date())
  -- Let's do latest year which has data
  strftime('%Y', soldDate) = (
    SELECT strftime('%Y', MAX(soldDate))
    FROM sales
    WHERE
      strftime('%m', soldDate) = strftime('%m', date())
      OR
      strftime('%m', soldDate) = strftime('%m', date('now','start of month','-1 month'))
  )
  AND 
  (
  strftime('%m', soldDate) = strftime('%m', date())
  OR
  strftime('%m', soldDate) = strftime('%m', date('now','start of month','-1 month'))
  )
GROUP BY strftime('%Y', soldDate), strftime('%m', soldDate)
ORDER BY month DESC;