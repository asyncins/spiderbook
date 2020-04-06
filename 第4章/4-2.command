# MySQL
CREATE TABLE WaitCrawl
(
    id int NOT NULL,
    name varchar(255) NOT NULL,
    url varchar(255) NOT NULL,
    UNIQUE (url)
);