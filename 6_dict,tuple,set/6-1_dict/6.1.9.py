while input() != 0:
    try:
        user_input = input("Enter something: ")
        print("You entered:", user_input)
    except EOFError:
        print("No input provided!")