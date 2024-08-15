SELECT signup_date, COUNT(id) as "count of users"
FROM users
GROUP BY signup_date;