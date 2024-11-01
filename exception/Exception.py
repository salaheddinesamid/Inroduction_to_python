def division_program():
    exit = False
    while not exit:
        try:
            number = int(input("Enter a number"))
            result = 5 / number
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!")
        except ValueError:
            print("Enter a valid number")
        finally:
            want_to_continue = input("Do you want to continue? [Y/n]?")
            if want_to_continue == "Y":
                exit = True
            elif want_to_continue == "n":
                exit = False

def reading_text_file():
    path = "/Users/salaheddine/Desktop/text_file"
    try:
        file = open(path,"r")
        content = file.read()
        print(content)
    except FileNotFoundError:
        print("File not found!")

    finally:
        file.close()
        print("File is closed")

reading_text_file()