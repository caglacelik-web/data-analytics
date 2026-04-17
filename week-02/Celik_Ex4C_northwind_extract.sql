-- Q4a) What is the name of the table that holds the items Northwind sells?
-- The table that holds items sold is Products
-- Q4b) What is the name of the table that holds the types/categories of the items Northwind sells?
-- The table that holds categories is Categories

-- Q5) 5.Create a SELECT statement to retrieve all columns from the employees table.
-- Q5a) Who is the Northwind employee whose name makes it look like she’s a bird?
SELECT * 
FROM Employees
-- The employee that looks like a bird is Margaret Peacock

-- Q6)Create a SELECT statement to retrieve all columns from the products table.
-- Q6a) How many records does your query return? Using the toolbar options at the top of the query pane, how can you change your query to retrieve only 10 rows? 
SELECT *
FROM Products 
-- This returns 77 rows
-- To limit results use LIMIT 10
-- Q6 BONUS: I used the LIMIT keyword in MySQL to restrict the number of rows returned.
-- I found this by using MySQL documentation / quick search.
SELECT * 
FROM Products 
	LIMIT 10;

-- Q7)Create another SELECT statement to retrieve all columns from the categories table.
-- Q7c)What is the category id of seafood? 
SELECT * 
FROM Categories
-- The category id of Seafood is 8

-- Q8a) Create a final SELECT statement to retrieve the top 50 records from orders, including only the OrderID, OrderDate, ShipName, and ShipCountry columns.

SELECT OrderID, OrderDate, ShipName, ShipCountry
FROM Orders
LIMIT 50