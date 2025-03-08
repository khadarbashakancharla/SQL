# Write your MySQL query statement below
-- select 
--     id 
-- from
--     (select 
--         id,
--         recordDate,
--         temperature,
--         LAG(temperature) over(order by recordDate) as previoustemp
--      from 
--         Weather
--     ) as temp_table
-- where
--     temperature > previoustemp    

select 
    w1.id 
from     
    Weather w1  
        join  
    Weather w2  on w1.recordDate = w2.recordDate + Interval 1 Day
where w2.temperature < w1.temperature   

