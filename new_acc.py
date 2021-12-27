import cx_Oracle
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style

conn = None

try:
    conn = cx_Oracle.connect(
        user='SYS',
        password='Kk9078123',
        mode=cx_Oracle.SYSDBA)
    print("connected")
except cx_Oracle.Error as error:
    print(error)

cursor = conn.cursor()


def new_acc():
    print("Вы выбрали ДОБАВИТЬ СЧЁТ:")
    new_acc2 = int(input("Введите новый аккаунт айди:"))
    new_cur2 = (input("Введите  валюта:"))

    try:
        val = (new_acc2, new_cur2, 0)
        sql = "insert into bnk values(to_number(:1),:2, to_number(:3))"
        cursor.execute(sql, tuple(val))
        conn.commit()
        print("Аккаунт создан.", val)
    except Exception:
        print("Tакой аккаунт существует.")


def transactions():
    print("Вы выбрали ВСЕ ТРАНЗАКЦИИ ПО СЧЕТУ:")
    id_acc_tr = int(input("Пожалуйста, введите аккаунт айди чтобы увидеть все транзакции по нему:"))
    query_acc_tr = "SELECT * FROM tr3 where idd={}".format(id_acc_tr)
    otchet_acc_tr = pd.read_sql(query_acc_tr, con=conn)
    print(otchet_acc_tr)


def transfer():
    cursor = conn.cursor()

    A = int(input("Пожалуйста, введите счет отправителя:"))
    B = int(input("Пожалуйста, введите счет получателя:"))
    money = int(input('Пожалуйста, введите сумму перевода:'))
    num = money
    try:
        cursor.execute('select money from bnk where idd={}'.format(A))
        a = int(cursor.fetchone()[0])
        cursor.execute('select money from bnk where idd={}'.format(B))
        b = int(cursor.fetchone()[0])
        currency_a = cursor.execute('select currency from bnk where idd={}'.format(A)).fetchone()[0]
        currency_b = cursor.execute('select currency from bnk where idd={}'.format(B)).fetchone()[0]

        if a < num:
            print("Перевод не выполнен, недостаточно остатка")
        else:
            if currency_b == currency_a:
                # таблица с историей изменения баланса
                val_1 = (A, currency_a, a - num)
                sql_1 = "insert into tr2 values(to_number(:1),:2, to_number(:3))"
                cursor.execute(sql_1, tuple(val_1))

                # все транзакции по id A
                val_1_1 = (A, currency_a, -num)
                sql_1_1 = "insert into tr3 values(to_number(:1),:2, to_number(:3))"
                cursor.execute(sql_1_1, tuple(val_1_1))

                # таблица с историей изменения баланса
                val_2 = (B, currency_b, b + num)
                sql_2 = "insert into tr2 values(to_number(:1), :2, to_number(:3))"
                cursor.execute(sql_2, tuple(val_2))

                # все транзакции по id B
                val_2_1 = (B, currency_b, num)
                sql_2_1 = "insert into tr3 values(to_number(:1), :2, to_number(:3))"
                cursor.execute(sql_2_1, tuple(val_2_1))

                cursor.execute('update bnk set money={} where idd={}'.format(a - num, A))
                cursor.execute('update bnk set money={} where idd={}'.format(b + num, B))
                conn.commit()  # change db
                print("Передача прошла успешно!")
            else:
                print("Деньги не переведено, разные валюты")
    except Exception:
        print("Перевод не выполнен, и транзакция была отменена. Проверьте айди счета!")
        conn.rollback()


def refill(): #ПОПОЛНЕНИЕ СЧЕТА
    cursor = conn.cursor()
    print("ВСЕ СЧЕТА:")
    print(pd.read_sql("SELECT * FROM bnk", con=conn))
    input_idd = int(input("Пожалуйста, введите аккаунт айди для пополнение:"))
    new_moneyy = int(input("Пожалуйста, введите сумму:"))
    old_moneyy = cursor.execute('select money from bnk where idd={}'.format(input_idd)).fetchone()[0]
    cursor = conn.cursor()
    cursor.execute('update bnk set money={} where idd={}'.format(old_moneyy + new_moneyy, input_idd))
    conn.commit()
    print("Аккаунт по ID номер {} пополнено на сумму {}. Доступно:{}".format(input_idd, new_moneyy,
                                                                             old_moneyy + new_moneyy))

def graph(): #ГРАФИК СЧЕТА
    A_graph = int(input("Пожалуйста, введите аккаунт айди для просмотра истории баланса:"))
    query = "SELECT * FROM tr2 where idd={}".format(A_graph)
    otchet = pd.read_sql(query, con=conn)
    otchet['MONEY'] = pd.to_numeric(otchet['MONEY'])
    x = otchet['MONEY']

    plt.xlabel(' ')
    plt.title('График историей изменения баланса по ID - {} '.format(A_graph))
    plt.ylabel('{}'.format(cursor.execute('select currency from bnk where idd={}'.format(A_graph)).fetchone()[0]))

    plt.plot(x)
    plt.show()



