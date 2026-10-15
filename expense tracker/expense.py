#expense tracker
import json
from datetime import datetime
import os
data={'income':[],'expenses':[]}

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
def save_expenses():
    with open("exp.json","w")as file:
        json.dump(data , file ,indent=4)
def load_expense():
    global data
    try:
        with open ("exp.json","r")as file:
            data=json.load(file)
            if 'income' not in data:
                data['income']=[]
            if 'expenses' not in data:
                data['expenses']=[]
    except FileNotFoundError:
        data={ 'income':[],'expenses' : []}
        return 
def add_income():
    try:
        income=int(input("Enter income: "))
    except ValueError:
        print("Invalid amount. Please enter a number.\n")
        return
    source=input("Enter source of income: ").strip()
    date=datetime.now().strftime("%d-%m-%y")
    inc={
        'income':income,
        'source':source,
        'date':date
    }
    data['income'].append(inc)
    save_expenses()
    print("---- Income added ----")
    
    
    


def add_expense():
        
        amount=float(input("Enter amount: $"))
        category=input(("Enter category: "))
        description=input("Enter description: ")
        date=datetime.now().strftime("%d-%m=%y")
        expense = {
            "amount": amount,
            "category": category,
            "description": description,
            "date":date
        }
        data['expenses'].append(expense)
        save_expenses()
        print("---- expense added successfully ----\n")

def view_expense():
    
    if not data['expenses']:
        print("expenses is empty")
    else:
        print("----- Youe Expenses -----")
        for i,expense in enumerate(data['expenses'],start=1):
            print(f"{i}. ${expense['amount']}")
            print(f"{expense['category']}")
            print(f"{expense['description']}")
            print(f"{expense['date']}")
            print("")

def delete_expense():
    
    view_expense()
    if not data['expenses']:
        print("Expenses is empty")
    else:
        ch=int(input("Enter expense no for delete: "))
        if 1<=ch<=len(data['expenses']):
            deleted=data['expenses'].pop(ch-1)
            save_expenses()
            print(" ==== Expense  deletion ====")
            print(f"amount: ${deleted['amount']}")
            print(f"Description: {deleted['description']}")
            print("\nexpense deleted successfully\n")
        else:
            print("Invalid expense no")

def filter_category():
    
    if not data['expenses']:
        print("Expense file is empty\n")
        return
    found=False
    cat=input("Enter category: ").lower()
    print(f"\n---- data by this catogary: {cat} ----\n")
    for i , expense in enumerate(data['expenses'],start=1):
        if expense['category']==cat:
            print(f"{i}. ${expense['amount']}")
            print(f"{expense['category']}")
            print(f"{expense['description']}")
            print(f"{expense['date']}")
            print("")
            found=True
    if not found:
        print("No expenses found by this category\n")
        

def balance_():
    total_income=0
    total_exp=0
    for income in data['income']:
        total_income+=income['income']
    for expense in data['expenses' ]:
        total_exp+=expense['amount']
    balance=total_income-total_exp   
    print("---- Total Balance ----")
    print(f"total income: {total_income}" )
    print(f"total expense: {total_exp}")
    print("="*20)
    
    print(f"Total Balance: {balance}")

def total_expense():
    
    total=0
    for expense in data['expenses']:
        total=total+expense['amount']
    print(f"Total expense: {total}\n")
    
    
    
    

   
load_expense()

while True:
    
    try:
        print("==== Menu ====\n")
        print("1. Add income \n2. Add expense \n3.View expense \n4. Delete expense \n5. Total expense \n6. Total Balane \n7. Filter by category \n8. Clear screen \n9. Exit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            add_income()
        elif choice==2:
            add_expense()
        elif choice==3:
            view_expense()
        elif choice==4:
            delete_expense()
        elif choice==5:
            total_expense()
        elif choice==6:
            balance_()    
        elif choice==7:
            filter_category()
        elif choice==8:
            clear_screen()
        elif choice==9:
            break    
        else:
            print("Invalid choice\n")
    except ValueError:
        print("\nplease enter an integer\n")

    
            