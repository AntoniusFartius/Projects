import random

path = "quotes.txt"
def help():
    print()
    print("What do you want to do?")
    print()
    print("0. Help")
    print("1. Give a random quote")
    print("2. Add a quote to the list")
    print("3. Path of the list")
    print("4. New path to list")
    print("5. Exit")

help()

while True:
    print()
    operation = input("Choose an operation: ")

    if operation == "0" or operation == "help":
        help()

    if operation == "1" or operation == "give":
        quotes = open(path).read().splitlines()
        print()
        print(random.choice(quotes))

    if operation == "2" or operation == "add":
        quotes = open(path, "a")
        quote = input("Enter the quote: ")
        if quote:
            quotes.write(quote + "\n")
            print("Quote added successfully!")
        else:
            print("No quote added.")
        quotes.close()
        
    if operation == "3" or operation == "path":
        print()
        print("The current path is:")
        print(path)

    if operation == "4" or operation == "new":
        print()
        path = input("Submit the new path: ")

    if operation == "5" or operation == "exit":
        exit()