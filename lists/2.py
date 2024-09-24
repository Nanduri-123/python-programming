expenses = [2200,2350,2600,2130,2190]

extra_feb = expenses[1]-expenses[0]
print(f"extra spent in february compared to january : ${extra_feb}")

total_first_quater = sum(expenses[:3])
print(f"Total expense in first quater: ${total_first_quater}")

exactly_2000 = 2000 in expenses
print(f"Spent exactly $2000 in any month: {exactly_2000}")

expenses.append(1980)
print(f"Updated expenses after adding June: {expenses}")

expenses[3] == 200
print(f"Updated expenses after refund in April: {expenses}")




