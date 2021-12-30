/* У нас должен быть 3 таблицы: 
bnk - аккаунт
tr2 - таблица с историей изменения баланса
tr3 - транзакция каждого аккаунта */


CREATE TABLE bnk (
    idd int NOT NULL PRIMARY KEY,
    currency varchar(255) NOT NULL,
    money int NOT NULL
);


CREATE TABLE tr2 (
    idd int NOT NULL,
    currency varchar(255) NOT NULL,
    money int NOT NULL
);



CREATE TABLE tr3 (
    idd int NOT NULL,
    currency varchar(255) NOT NULL,
    money int NOT NULL
);




select * FROM bnk;

select * FROM tr2;

select * FROM tr3;
