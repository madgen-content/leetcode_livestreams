/* +---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| ad_id         | int     |
| user_id       | int     |
| action        | enum    |
+---------------+---------+ */

SELECT
    ad_id,
    ROUND(
        COALESCE(
            SUM(IF(action = "Clicked", 1, 0)) / 
            ( 
            SUM(IF(action = "Clicked", 1, 0)) + 
            SUM(IF(action = "Viewed", 1, 0))
            ) 
            * 100
        , 0)
    , 2) as ctr
FROM Ads
GROUP BY ad_id
ORDER BY ctr desc, ad_id asc
HAVING ctr > 0 