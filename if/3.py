sugar = int(input("Enter the fasting level :"))

if sugar in range(80,101):
    print("Sugar is normal")
elif sugar > 100:
    print("Sugar is high")
else:
    print("Sugar is low")
   

