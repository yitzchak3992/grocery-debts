import csv
import threading
from customer import Customer
from binary_search_tree import Tree


main_title = ["name", "last_name", "id", "phone", "debt", "date"]
"""
data =[["yitzchak" ,"abalas" ,123456789 ,"0510101010" ,"31/12/2023" ,-44] ,
       ["yosef" ,"Salton" ,123465679 ,"0520101010" ,"01/12/2023" ,-21] ,
       ["yitzchak" ,"abalas" ,123456789 ,"0510101010" ,"31/12/2023" ,70] ,
       ["yitzchak" ,"abalas" ,123456789 ,"0510101010" ,"31/12/2023" ,-15] ,]

#data = [[name,last_name,id,phone,date,debt]]
with open("shop.csv" ,"w" ,newline="")as csvfiie:
    # יצירת כותב CSV
    writer = csv.writer(csvfiie)

    # כתיבת הכותרת
    writer.writerow(main_title)

    # כתיבת שאר הנתונים
    for row in data:
        writer.writerow(row)
"""
data_base_tree = Tree()
with open("shop.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # You need to check for correctness !!!

        if row == main_title:
            continue
        row[-1] = float(row[-1])
        customer = data_base_tree.search_id(row[2])
        if customer:
            customer.add_debt(row[-1])
        else:
            customer = Customer(*row)
            data_base_tree.add_node(customer)

print(data_base_tree)
