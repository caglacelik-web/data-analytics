USE northwind
-- 1. Write a query to find the price of the cheapest item that Northwind sells. Then write a second query to find the name of the product that has that price.
SELECT MIN(UnitPrice) -- 2.5000
FROM products

SELECT ProductName, UnitPrice
FROM products
WHERE UnitPrice = (SELECT MIN(UnitPrice) FROM products) -- Geitost

-- 2. Write a query to find the average price of all items that Northwind sells.

SELECT ROUND(AVG(UnitPrice), 2)
FROM products -- 28.87

-- 3. Write a query to find the price of the most expensive item that Northwind sells. Then write a second query to find the name of the product with that price, plus the name of the supplier for that product.
SELECT MAX(UnitPrice)
FROM Products -- 263.5000

SELECT products.ProductName,
       products.UnitPrice,
       suppliers.CompanyName
FROM products
JOIN suppliers
ON products.SupplierID = suppliers.SupplierID 
WHERE products.UnitPrice = (SELECT MAX(UnitPrice) FROM products)

-- 4. Write a query to find total monthly payroll (the sum of all the employees’ monthly salaries)
SELECT SUM(Salary)
FROM Employees

SELECT CONCAT('$', FORMAT(SUM(Salary), 2)) AS TotalPayroll
FROM employees -- $20,362.93

-- 5. Write a query to identify the highest salary and the lowest salary amounts which any employee makes. (Just the amounts, not the specific employees!)
SELECT MAX(Salary), MIN(Salary)
FROM employees

SELECT 
    CONCAT('$', FORMAT(MAX(Salary), 2)) AS MaxSalary,
    CONCAT('$', FORMAT(MIN(Salary), 2)) AS MinSalary
FROM employees
-- $3,119.15 max, $1,744.21 min

-- 6. Write a query to find the name and supplier ID of each supplier and the number of items they supply. Hint: Join is your friend here.
SELECT suppliers.CompanyName,
       suppliers.SupplierID,
       COUNT(products.ProductID) AS ProductCount
FROM suppliers
JOIN products
ON suppliers.SupplierID = products.SupplierID
GROUP BY suppliers.CompanyName, suppliers.SupplierID

-- 7. Write a query to find the list of all category names and the average price for items in each category.
SELECT categories.CategoryName, AVG(products.UnitPrice) AS AvgPrice
FROM products
JOIN categories
ON products.CategoryID = categories.CategoryID
GROUP BY categories.CategoryName

-- 8. Write a query to find, for all suppliers that provide at least 5 items to Northwind, what is the name of each supplier and the number of items they supply.
SELECT suppliers.CompanyName, COUNT(products.ProductID) AS ProductCount
FROM suppliers
JOIN products
ON suppliers.SupplierID = products.SupplierID
GROUP BY suppliers.CompanyName
HAVING COUNT(products.ProductID) >= 5

-- 9. Write a query to list products currently in inventory by the product id, product name, and inventory value. Sort the results in descending order by value.
SELECT ProductID, ProductName, ROUND(UnitPrice * UnitsInStock, 2) AS InventoryValue
FROM products
WHERE UnitsInStock > 0
ORDER BY InventoryValue DESC, ProductName

