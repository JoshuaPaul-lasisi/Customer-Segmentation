CREATE TABLE customer_segments (
    customer_id INT PRIMARY KEY,
    num_purchases INT,
    total_quantity INT,
    total_price FLOAT,
    cluster INT
);
