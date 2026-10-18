name = input("Enter your Name = ")
sub1 = float(input("Enter the Marks of Computer Science = "))
sub2 = float(input("Enter the Marks of English = "))
sub3 = float(input("Enter the Marks of Math = "))
total = sub1 + sub2 + sub3
per = (total / 300) * 100
print("============ Student Marks Calculator ===============")
print("Total Marks = ",total)
print("Percentage = ",per, " % ")