-- Product

-- +--------------+---------+
-- | Column Name  | Type    |
-- +--------------+---------+
-- | product_id   | int     |
-- | product_name | varchar |
-- | unit_price   | int     |
-- +--------------+---------+
-- Table: Sales

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | seller_id   | int     |
-- | product_id  | int     |
-- | buyer_id    | int     |
-- | sale_date   | date    |
-- | quantity    | int     |
-- | price       | int     |
-- +-------------+---------+
-- # Write your MySQL query statement below
SELECT buyer_id
FROM 
(
    SELECT
    S.buyer_id,
    sum(case when product_name="S8" then 1 else 0 end) s8_freq,
    sum(case when product_name="iPhone" then 1 else 0 end) iphone_freq
    FROM SALES S
    Left Join Product P
    on P.product_id = S.product_id
    GROUP BY S.buyer_id
    HAVING s8_freq > 0
        AND iphone_freq = 0
) final