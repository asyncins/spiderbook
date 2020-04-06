# MySQL
> insert into WaitCrawl (id, name, url) VALUES (1, "exam", "http://exam.com");
Query OK, 1 row affected (0.01 sec)
> insert into WaitCrawl (id, name, url) VALUES (2, "exam", "http://exam.com");
ERROR 1062 (23000): Duplicate entry 'http://exam.com' for key 'url'