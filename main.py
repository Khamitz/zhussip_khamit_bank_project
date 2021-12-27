import cx_Oracle
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style
from new_acc import new_acc, transactions, transfer, refill, graph


if __name__ == '__main__':
    conn = cx_Oracle.connect(user='SYS', password='Kk9078123', mode=cx_Oracle.SYSDBA)

    cursor = conn.cursor()
    cursor.execute("select * from bnk")
    print("ВСЕ СЧЕТА:")
    print(pd.read_sql("SELECT * FROM bnk ", con=conn))
    print("МАКСИМАЛЬНЫЕ ДЕНЬГИ ПО ВАЛЮТАМ:")
    print(pd.read_sql("SELECT currency, max(money) as Max_Money FROM bnk GROUP BY currency", con=conn))


    print("\n Выберите операцию: \n 1-добавить счёт \n 2-все транзакции по счету \n 3-перевод деньги по счету"
          " \n 4-пополнить счет \n 5-график историей изменения баланса ")
    enter1 = int(input("Напишите сюда номер операцию:"))
    if enter1 == 1:  #Добавить счёт
        new_acc()
    elif enter1 == 2:  #ВСЕ ТРАНЗАКЦИИ ПО СЧЕТУ
        transactions()
    elif enter1 == 3:  #ПЕРЕВОД
        transfer()
    elif enter1 == 4:  #ПОПОЛНЕНИЕ СЧЕТА
        refill()
    elif enter1 == 5:  #ГРАФИК
        graph()
    else:
        print("дурыс тандау керек еды:")

