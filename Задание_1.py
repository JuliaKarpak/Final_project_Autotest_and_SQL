# \dt - список таблиц в БД
# SELECT * FROM "Couriers"; - проверка созданных курьеров
# SELECT * FROM "Orders"; - проверка созданных заказов
# SELECT * FROM "Orders" WHERE "inDelivery"=true; - проверка принятых заказов
# SELECT c.login, COUNT(o.id) 
#     FROM "Couriers" AS c 
#     LEFT OUTER JOIN "Orders" AS o ON c.id=o."courierId" 
#     WHERE o."inDelivery"=true 
#     GROUP BY c.login; 
# - список логинов курьеров с кол-м принях заказов