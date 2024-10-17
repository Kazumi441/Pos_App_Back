CREATE DATABASE pos_system;

USE pos_system;

CREATE TABLE product (
    id INT PRIMARY KEY AUTO_INCREMENT,
    code VARCHAR(13) NOT NULL UNIQUE,
    name VARCHAR(50) NOT NULL,
    price INT NOT NULL
);

CREATE TABLE purchase (
    id INT PRIMARY KEY AUTO_INCREMENT,
    total INT NOT NULL,
    total_excl_tax INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE purchase_item (
    id INT PRIMARY KEY AUTO_INCREMENT,
    purchase_id INT,
    product_id INT,
    FOREIGN KEY (purchase_id) REFERENCES purchase(id),
    FOREIGN KEY (product_id) REFERENCES product(id)
);
