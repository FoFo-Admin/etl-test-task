CREATE TABLE IF NOT EXISTS users(
	id INT PRIMARY KEY,
	full_name VARCHAR(100) NOT NULL,
	email VARCHAR(200) NOT NULL UNIQUE,
	signup_date DATE NOT NULL,
	domain VARCHAR(50) NOT NULL
);