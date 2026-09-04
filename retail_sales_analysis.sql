--Revenue by month
SELECT order_month, SUM("Total Spent") AS revenue
FROM sales 
GROUP BY order_month
ORDER BY order_month;

--Top categories by revenue
SELECT category, SUM("Total Spent") AS revenue, COUNT(*) AS transactions
FROM sales
GROUP BY category
ORDER BY revenue DESC;

--Online vs. in-store performance by category
SELECT category, location, SUM("Total Spent") AS revenue,
    ROUND(AVG("Total Spent"), 2) AS avg_order_value
FROM sales
GROUP BY category, location
ORDER BY category, location;

--Repeat vs. new customers
SELECT is_repeat, COUNT(DISTINCT "Customer ID") AS customers,
    SUM("Total Spent") AS revenue
FROM sales
GROUP BY is_repeat;

--Discount impact on quantity and order value
SELECT discount_status, ROUND(AVG(quantity), 2) AS avg_quantity, ROUND(AVG("Total Spent"),2) AS avg_order_value
FROM sales
GROUP BY discount_status;