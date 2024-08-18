CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100),
    manager_id INT
);

--Insert data into employees table

INSERT INTO employees (emp_id, emp_name, manager_id) VALUES
(1, 'Alice Smith', NULL),     -- Top-level manager (CEO)
(2, 'Bob Johnson', 1),       -- Direct report to Alice
(3, 'Charlie Davis', 1),     -- Direct report to Alice
(4, 'David Wilson', 2),      -- Direct report to Bob
(5, 'Eva Martinez', 2),      -- Direct report to Bob
(6, 'Frank Lewis', 3),       -- Direct report to Charlie
(7, 'Grace Lee', 3);         -- Direct report to Charlie

