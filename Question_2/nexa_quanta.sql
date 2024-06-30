CREATE DATABASE nexaquanta;
USE nexaquanta;
CREATE TABLE Customer (customer_id INT NOT NULL,product_key INT NOT NULL);
CREATE TABLE Product (product_key INT PRIMARY KEY);

INSERT INTO Customer (customer_id, product_key) VALUES (1, 5), (2, 6), (3, 5), (3, 6), (1, 6);
INSERT INTO Product (product_key) VALUES (5), (6);

%%% Solution %%%

-- Query to find customers who bought all the products
WITH TotalProducts AS (SELECT COUNT(*) AS total_count FROM Product),
CustomerProductCounts AS (
    SELECT customer_id, COUNT(DISTINCT product_key) AS product_count
    FROM Customer
    GROUP BY customer_id
)
SELECT c.customer_id
FROM CustomerProductCounts c, TotalProducts t
WHERE c.product_count = t.total_count;
