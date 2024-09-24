#Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred. If expense is not found then it should print that as well.
exp = int(input("Enter the expense amount :"))
expense_list = [2340,2500,2100,3100,2980]
month_list = ["January","February","March","April","May"]

for i in range(5):
    if exp == expense_list[i]:
        print("Expense amount is in month of:",month_list[i])
    else:
        print("Expense amount is not in list")
    break
    