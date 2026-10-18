name = input("Enter your Name = ")
birth_year = int(input("Enter your Birth Year = "))
current_year = int(input("Enter your Current Year = "))
city = input("Enter your City Name = ")

uppercase = name.upper()
lowercase = name.lower()
age = current_year - birth_year
is_adult = age >= 18
length_name = len(name)

print("------------- Personal Profile Generator -----------------------")
print("Name ( Uppercase ) = ",uppercase)
print("Name ( Lowercase ) = ",lowercase)
print("City Name = ",city)
print("Age = ",age)
print("Adult ( 18 + ) = ",is_adult)
print("Name Length = ",length_name)