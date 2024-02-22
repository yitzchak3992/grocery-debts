import csv
import threading
from customer import Customer
from binary_search_tree import Tree
import sys
import os

main_title = ["name", "last_name", "id", "phone", "debt", "date"]

data = [
    ["yitzchak", "abalas", 123456789, "0510101010", "31/12/2023", -44],
    ["yosef", "Salton", 123465679, "0520101010", "01/12/2023", -21],
    ["yitzchak", "abalas", 123456789, "0510101010", "31/12/2023", 70],
    ["yitzchak", "abalas", 123456789, "0510101010", "31/12/2023", -15],
]
"""
if sys.argv < 2:
    print("Error: No file typed")
    quit()

file_name = sys.argv[1]
if not os.path.exists(file_name):
    with open(file_name ,"w" ,newline="")as csvfiie:
        pass    
"""


# with open("shop.csv" ,"w" ,newline="")as csvfiie:
#     writer = csv.writer(csvfiie)
#     # Writing the title
#     writer.writerow(main_title)
#     # Writing the rest of the data
#     for row in data:
#         writer.writerow(row)


def check_validity(row: list[str]):
    if len(row) != 6:
        print(
            """Error: 6 parameters must be entered in this format: \n'name', 'last_name', 'id', 'phone', 'debt', 'date'"""
        )
        return False
    for i in range(5):  # Deletes unnecessary spaces
        row[i] = row[i].strip()
    row[0], row[1] = row[0].lower(), row[1].lower()  # Convert the letters to lowercase

    if len(row[2]) != 9 or not row[2].isdigit():
        print("The id must be 9 digits!")
        row[2] = input("Type ID in standard form: ")
        check_validity(row)
    if row[3][0] != "0" or len(row[3]) != 10:
        print("Error: Phone number must start with 0 and have 10 digits!")
        row[3] = input("Type Phone in standard form:")
        check_validity(row)
    return Tree


def customer_document(row: list[str]):
    with open("shop.csv", "a", newline="") as csvfiie:
        writer = csv.writer(csvfiie)
        writer.writerow(row)


data_base_tree = Tree()

# with open("file_name", "r") as csvfile:
with open("shop.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # You need to check for correctness !!!

        if row == main_title:
            continue
        if check_validity(row):
            data_base_tree.set_customer(row)

while Tree:
    command = input(
        """ Optional commands:
                    1.print (print by debt)
                    2.set (The fields must be filled in correctly)
                    3.id (print by id)
                    4.select
                    0.quit
                    ->: """
    )
    command, _, fields = command.partition(" ")
    fields = fields.split(" ")

    if command == "print" or command == "1":
        data_base_tree.print_by_debt()

    if command == "set" or command == "2":
        if check_validity(fields):
            if data_base_tree.set_customer(fields):
                customer_document(fields)

    if command == "id" or command == "3":
        print(data_base_tree)

    if command == "quit" or command == "0":
        quit()
