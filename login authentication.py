def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    
    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")
    
    print("Registration successful!")


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    with open("users.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(',')
            if username == stored_username and password == stored_password:
                print("Login successful!")
                return username  # Return the username if login is successful
        print("Invalid credentials. Please try again.")
        return None  # Return None if login fails

def secured_page(username):
    print(f"Welcome to the secured page, {username}!")

def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Select an option: ")
        
        if choice == '1':
            register()
        elif choice == '2':
            username = login()  # Get the username returned by the login function
            if username is not None:
                secured_page(username)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
#the datas like password and username in the format of username,password will be stored in 'users.txt' file
