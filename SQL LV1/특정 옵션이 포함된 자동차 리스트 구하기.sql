SELECT CAR_ID,car_type	,daily_fee,options
FROM CAR_RENTAL_COMPANY_CAR 
where OPTIONS like '%네비게이션%'
ORDER BY CAR_ID DESC