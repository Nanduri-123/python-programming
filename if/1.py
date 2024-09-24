city = input("Enter the city name :")

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

if city in india:
    print("City is in India")
elif city in pakistan:
    print("City is in pakistan")
elif city in bangladesh:
    print("City is in Bangladesh")
else:
    print("Based on provided data there is no specified city")
