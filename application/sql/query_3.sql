SELECT *
FROM users
WHERE signup_date BETWEEN NOW() - interval '7 days' AND NOW();