server_username="sky"
server_user_password="123"

user_entered_username=input("Enter your username: ")
user_entered_password=input("Enter your password: ")

if(server_username == user_entered_username and server_user_password == user_entered_password):
   print("You are logged in") 
else:
    print("Your username or password is incorrect")