print("FOLLOW THE INSTRUCTIONS TO FIND THE USER")
print("*************************************************************")

In1="To search by ID: Go to Facebook.com and find the UserID which would look something like this: 10003340872XXXX"
In2="To search by Username: Use the format First_name:Last_name"
In3="To Filter by City: Use the format: City"
print(In1)
print(In2)
print(In3)

print("*************************************************************")

#Taking the user input of the parameter to search from
id = input("Enter the Parameter to search for the user:")

#Adding the database file of the leaked Data. If you want to add more database text files, youu can add it here.
file_a = open(".\India 1.txt" , encoding="utf8")
file_b = open(".\India 2.txt" , encoding="utf8")

#Creating the function the read the database and print the result.
for line in file_a and file_b: #enter your database file here.
    if id in line:
        print("Your Data Has Been Compromised")
        print("*************************************************************")
        print(line)
        print("*************************************************************")
        break

#if no matching results are found:
if id not in line:
    print("Your Data is Safe")
