def greet_user(name):
    print(f"Hello, {name}!")

    if name:
        print("Name is provided.")
    
    print("End of function.")  # This should be outside the if block

greet_user("Alice")
