# program that prompts the user to enter a password. Keep prompting the user until they enter the correct password "abc123". Once the correct password is entered, print a success message.

while True:
   password = input("Enter password: ")
   if password == 'abc123':
      break
   else:
       print("Your password is wrong please try again.")

print("Congratulations on your incredible success! ...")