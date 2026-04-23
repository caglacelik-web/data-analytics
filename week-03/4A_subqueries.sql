USE northwind
-- 1. What is the product name(s) of the most expensive products?
SELECT MAX(UnitPrice)
FROM products

SELECT ProductName
FROM products
WHERE UnitPrice = (SELECT MAX(UnitPrice)FROM products) 
-- Cte de Blaye

-- 2. What is the product name(s) and categories of the least expensive products?
SELECT products.ProductName, categories.CategoryName
FROM products
JOIN categories
ON products.CategoryID = categories.CategoryID
WHERE products.UnitPrice = (SELECT MIN(UnitPrice)FROM products)
-- Geitost, Dairy Products

-- 3. What is the order id, shipping name and shipping address of all orders shipped via "Federal Shipping"?
SELECT ShipperID
FROM shippers
WHERE CompanyName = 'Federal Shipping' -- 3

SELECT OrderID, ShipName, ShipAddress
FROM orders
WHERE ShipVia = (SELECT ShipperID FROM shippers WHERE CompanyName = 'Federal Shipping') -- 255 rows 

-- 4. What are the order ids of the orders that included "Sasquatch Ale"?
SELECT ProductID
FROM products
WHERE ProductName = 'Sasquatch Ale' -- 34

SELECT OrderID
FROM `order details`
WHERE ProductID = (SELECT ProductID FROM products WHERE ProductName = 'Sasquatch Ale') -- 19 rows

-- 5. What is the name of the employee that sold order 10266?

SELECT FirstName, LastName
FROM employees
WHERE EmployeeID = (SELECT EmployeeID FROM orders WHERE OrderID = 10266) -- Janet Leverling

-- 6. What is the name of the customer that bought order 10266?
SELECT CompanyName
FROM customers
WHERE CustomerID = (SELECT CustomerID FROM orders WHERE OrderID = 10266) -- Wartian Herkku
