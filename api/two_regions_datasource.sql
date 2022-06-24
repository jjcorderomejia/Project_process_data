
--From the two most commonly appearing regions, which is the latest datasource?
    
select region, datasource
FROM(
    select region, datasource, 
    row_number() over(partition by region order by `datetime` desc) row_value
    from  `api_trips`
    where region in 
            (select region 
            FROM(
                select region,
                row_number() over(order by total desc) row_value
                from
                    (
                    SELECT region, count(1) total
                    FROM `api_trips` 
                    group by region
                        ) a
                ) B
           WHERE ROW_VALUE <= 2
           )
   ) C
   where ROW_VALUE = 1
