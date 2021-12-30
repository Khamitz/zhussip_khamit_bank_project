у нас должен быть 3 таблицы: bnk, tr2, tr3.

CREATE TABLE bnk (
    idd int NOT NULL PRIMARY KEY,
    currency varchar(255) NOT NULL,
    money int NOT NULL
);  --аккаунт


CREATE TABLE tr2 (
    idd int NOT NULL,
    currency varchar(255) NOT NULL,
    money int NOT NULL
);       -- таблица с историей изменения баланса. 



CREATE TABLE tr3 (
    idd int NOT NULL,
    currency varchar(255) NOT NULL,
    money int NOT NULL
);    --транзакция каждого аккаунта


select * FROM bnk; --аккаунт

select * FROM tr2;  -- таблица с историей изменения баланса. 

select * FROM tr3; --транзакция каждого аккаунта