SELECT HOUR(DATETIME) as HOUR, COUNT(DateTime) AS COUNT
FROM ANIMAL_OUTS
GROUP BY HOUR
HAVING HOUR >=9 and HOUR <= 19
ORDER BY HOUR