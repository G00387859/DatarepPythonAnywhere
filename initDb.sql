use datarepresentation;
    CREATE TABLE store (
    id int NOT NULL auto_increment,
    productType VARCHAR(100),
    productName varchar(100),
    productPrice float(4),
    PRIMARY KEY(id),
    UNIQUE KEY unique_productName (productName)
);

    