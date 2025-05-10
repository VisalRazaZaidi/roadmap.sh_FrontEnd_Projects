def add():
    name = input("Name: ")
    password = input("Password: ")

    with open("password.txt", "a") as f:
        f.write(f"{name} | {password}\n")

def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()    # rstrip() remove the character return
            user, code = data.split("|")
            print(f"User = {user}\nPassword = {code}")

while True:
    mode = input("Would you like to add a new password or view existing one? (view, add) or Q to quit: ").lower()

    if mode == "q":
        quit()

    elif mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("Invalid Mode!")
        continue
