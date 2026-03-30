/*Top proizvodi po prodaji*/
SELECT 
    product_id,
    SUM(quantity) AS total_sold,
    SUM(revenue) AS total_revenue
FROM sales
GROUP BY product_id
ORDER BY total_revenue DESC;

/*Prodaja po danima (trend)*/
SELECT 
    date,
    SUM(revenue) AS daily_revenue
FROM sales
GROUP BY date
ORDER BY date;

/*Join sa inventory*/
SELECT 
    s.product_id,
    SUM(s.quantity) AS sold,
    i.stock_quantity
FROM sales s
JOIN inventory i 
ON s.product_id = i.product_id
GROUP BY s.product_id, i.stock_quantity;

/*Proizvodi koji će uskoro nestati*/
SELECT 
    s.product_id,
    SUM(s.quantity)/COUNT(DISTINCT s.date) AS avg_daily_sales,
    i.stock_quantity
FROM sales s
JOIN inventory i ON s.product_id = i.product_id
GROUP BY s.product_id, i.stock_quantity
HAVING i.stock_quantity < avg_daily_sales * 7;

/*Najslabiji proizvodi*/
SELECT 
    product_id,
    SUM(quantity) AS total_sold
FROM sales
GROUP BY product_id
ORDER BY total_sold ASC
LIMIT 5;

/*Proizvodi koji se ne prodaju dobro ali imaju puno zaliha*/
SELECT 
    s.product_id,
    SUM(s.quantity) AS sold,
    i.stock_quantity
FROM sales s
JOIN inventory i ON s.product_id = i.product_id
GROUP BY s.product_id, i.stock_quantity
HAVING sold < 10 AND i.stock_quantity > 30;