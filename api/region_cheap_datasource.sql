
--What regions has the "cheap_mobile" datasource appeared in?

SELECT distinct region
FROM `api_trips` 
WHERE datasource in ('cheap_mobile')