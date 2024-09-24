countries_population = {'china': 143,'india': 136,'usa': 32,'pakistan':21} 

def print_population():
    for country,population in countries_population.items():
        print(f"{country} ==> {population}")

def add_country():
    country = input("Enter the country name to add:").strip().lower()
    if country in countries_population:
        print(f"{country} already exists in the dataset.")
    else:
        population = int(input(f"Enter the population for {country}"))
        population = countries_population[country]
        print(f"Added {country} with population {population}.")

def remove_country():
     country = input("Enter the country name to remove:").strip().lower()
     if country in countries_population:
           del countries_population[country]
           print(f"Removed {country}. New dataset:")
           print_population()
     else:
          print(f"{country} does not exist in dataset.")

def query_population():
    country = input("Enter a country name to query:").strip().lower()
    if country in countries_population:
        print(f"The population of {country} is {countries_population[country]}")
    else:
        print(f"{country} does not exist in the dataset.")

while True:
    command = input("Enter a command (print,add,remove,qeury,exit):").strip().lower()
    if command == "print":
        print_population()
    elif command == "add":
        add_country()
    elif command == "remove":
        remove_country()
    elif command == "query":
        query_population()
    elif command == "exit":
        break
    else :
        print("Invalid command. Please try again.")
                



 


