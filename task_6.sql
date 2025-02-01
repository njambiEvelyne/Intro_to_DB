-- Use the database passed as argument
-- Create the customer table if it doesn't exist
CREATE TABLE IF NOT EXISTS customer (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(215),
    email VARCHAR(215),
    address TEXT
);
-- Use the database passed as argument
USE alx_book_store;

-- Insert multiple rows into the customer table
INSERT INTO customer (customer_id, customer_name, email, address)
VALUES
(2, 'Blessing Malik', 'bmalik@sandtech.com', '124 Happiness Ave.'),
(3, 'Obed Ehoneah', 'eobed@sandtech.com', '125 Happiness Ave.'),
(4, 'Nehemial Kamolu', 'nkamolu@sandtech.com', '126 Happiness Ave.');
