def describe_city(city: str, country: str):
    
    print(f"\n{city} is in {country}.")
    
describe_city(city = input("Enter the city: ").capitalize(), country = input("Enter the country: ").capitalize())