city1 = input("Enter the city1 name :")
city2 = input("Enter the city2 name :")

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

if city1 in india and city2 in india:
    print("Both cities are in India")
elif city1 in pakistan and city2 in pakistan:
    print("Both cities are in pakistan")
elif city1 in bangladesh and city2 in bangladesh:
    print("Both cities are in bangladesh")
else:
    print("Both cties are not in same city")