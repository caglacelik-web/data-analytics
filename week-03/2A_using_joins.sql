USE northwind
-- 1. Create a single query to list the product id, product name, unit price and category name of all products. Order by category name and within that, by product name.
SELECT products.ProductID,
       products.ProductName,
       products.UnitPrice,
       categories.CategoryName
FROM products
JOIN categories
ON products.CategoryID = categories.CategoryID
ORDER BY categories.CategoryName, products.ProductName

-- 2. Create a single query to list the product id, product name, unit price and supplier name of all products that cost more than $75. Order by product name.
SELECT products.ProductID,
       products.ProductName,
       products.UnitPrice,
       suppliers.CompanyName
FROM products
JOIN suppliers
ON products.SupplierID = suppliers.SupplierID
WHERE products.UnitPrice > 75
ORDER BY products.ProductName

-- 3. Create a single query to list the product id, product name, unit price, category name, and supplier name of every product. Order by product name.
SELECT products.ProductID,
       products.ProductName,
       products.UnitPrice,
       categories.CategoryName,
       suppliers.CompanyName
FROM products
JOIN categories
ON products.CategoryID = categories.CategoryID
JOIN suppliers
ON products.SupplierID = suppliers.SupplierID
ORDER BY products.ProductName
       
-- 4. Create a single query to list the order id, ship name, ship address, and shipping company name of every order that shipped to Germany. Assign the shipping company name the alias ‘Shipper.’ Order by the name of the shipper, then the name of who it shipped to
SELECT o.OrderID, o.ShipName, o.ShipAddress,
       s.CompanyName AS Shipper
FROM orders o
JOIN shippers s
ON o.ShipVia = s.ShipperID
WHERE o.ShipCountry = 'Germany'
ORDER BY Shipper, o.ShipName

-- 5. Start from the same query as above (#4), but omit OrderID and add logic to group by ship name, with a count of how many orders were shipped for that ship name
SELECT o.ShipName, COUNT(*) AS OrderCount
FROM orders o
JOIN shippers s
ON o.ShipVia = s.ShipperID
WHERE o.ShipCountry = 'Germany'
GROUP BY o.ShipName

-- 6. Create a single query to list the order id, order date, ship name, ship address of all orders that included Sasquatch Ale.
SELECT orders.OrderID,
       orders.OrderDate,
       orders.ShipName,
       orders.ShipAddress
FROM orders
JOIN `order details`
ON orders.OrderID = `order details`.OrderID
JOIN products
ON `order details`.ProductID = products.ProductID
WHERE products.ProductName = 'Sasquatch Ale'
