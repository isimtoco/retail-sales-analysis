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

--Repeat vs. new customers
--Customer concentration: Does the top 20% of customers drive most of the revenue?
--Discount impact on quantity and order value