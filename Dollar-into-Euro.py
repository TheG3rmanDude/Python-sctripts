# Dollar into Euro.

# Import inputimeout and TimeoutOccurred from the inputimeout module.
from inputimeout import inputimeout, TimeoutOccurred

# Ask user to chose language
print("\nHello, please choose a language / Bitte wählen Sie eine Sprache: English/Deutsch \n")

# Ask user to input language and timeout if the user takes longer than 160 seconds.
language = inputimeout(prompt = 'Language: ', timeout = 160)





# Code block if the user chose english.
if "Eng" in language or "eng" in language:

    # GENEREAL STUFF

    # Tell the user that they have chosen english.
    print("\nYou have chosen: 'English'. \n")
    # Ask the user what dollar amount they want converted.
    print("What dollar amount do you want converted?")
    # Take the dollar amount input, convert it into a float and save it in a variable.
    dollar = float(inputimeout(prompt = 'please enter an amount:  '))
    # Calculate the euro amount from the dollar input.
    euro = dollar / 1.0879
    # Round the result to two decimal places.
    euro = round(euro,2)
    
    
    
    # STARTING THE USER INPUT SECTION

    # Ask the user for confirmation.
    print("\nYou want to know how much " + str(dollar) + " are in Euro?")
    # Take the users anwser as input to later do some logical operations with it.
    confirmation = inputimeout(prompt = 'Y / N   ')



    # CONFIRMATION SECTION:

    # If the user chose yes for the confirmation:
    if "Y" in confirmation or "y" in confirmation:
        # display the dollar amount and the equivilant amount of euros,
        print('Sure thing!')
        print(str(dollar) +"$" + " are about " + str(euro) + "€. ")
        # ask the user if they want to know the formular,
        print("\nDo you want to know the formular?")
        # take the users input,
        formular = inputimeout(prompt = 'Y / N   ')
        #, if the input is yes:
        if "Y" in formular or "y" in formular:
            # display the formular and say goodbye.
            print("The formular is '[dollar] ÷ 1.0879 = Euro'. \n")
            print("Thank you for the task, goodbye!")
        #, else if the input is no:
        elif "N" in formular or "n" in formular:
            # say okay, thank the user for the task and say goodbye.
            print("Okay")
            print("\nThank you for the task. Goodbye!")
        #, else raise an Error telling the user that they have entered an invalid expression.
        else:
            raise SyntaxError("Invalid expression.")

    # Else if the user chose no for the confirmation:
    elif "N" in confirmation or "n" in confirmation:
        # ask the user if they still want to know the formular,
        print("\nOkay, would you still like to know the formular?")
        # take the users anwser as input,
        still_formular = inputimeout(prompt = 'Y / N   ')
        # if they still want to know the formular:
        if "Y" in still_formular or "y" in still_formular:
            # display the formular and say goodbye.
            print("The formular is '[dollar] ÷ 1.0879 = euro'. \n")
            print("Thank you for the task, goodbye!")
        # else if they don't want to know the formular:
        elif "N" in still_formular or "n" in still_formular:
            # say goodbye.
            print("\nAlright, goodbye!")
        # else raise an Error telling the user that they have entered an invalid expression.
        else:
            raise SyntaxError("Invalid expression.")





            # CODE IN GERMAN
            
# Code block if the user chose german:
elif "de" in language or "De" in language:

        # GENEREAL STUFF

    # Tell the user that they have chosen german.
    print(f"Sie wählten: 'Deutsch'. \n")
    # Ask the user what dollar amount they want converted.
    print("Wie viele Dollar möchten Sie in Euro umgewandelt haben?")
    # Take the dollar amount input, convert it into a float and save it in a variable.
    dollar = float(inputimeout(prompt = 'Bitte geben Sie einen Betrag ein: '))
    # Calculate the euro amount from the dollar input.
    euro = dollar / 1.0879
    # Round the result to two decimal places.
    euro = round(euro,2)



    # STARTING THE USER INPUT SECTION
    
    # Ask the user for confirmation.
    print(f"\nSie möchten wissen, wie viel ${dollar} in Euro sind?")
    # Take the users anwser as input to later do some logical operations with it.
    confirmation = inputimeout(prompt = 'J / N   ')



    # CONFIRMATION SECTION:

    # If the user chose yes for the confirmation:
    if "J" in confirmation or "j" in confirmation:
        # display the dollar amount and the equivilant amount of euros,
        print('\nKein Problem!')
        print(f"${dollar} sind etwa {euro}€.")
        # ask the user if they want to know the formular,
        print("\nMöchten Sie die Formel wissen?")
        # take the users input,
        formular = inputimeout(prompt = 'J / N   ')
        #, if the input is yes:
        if "J" in formular or "j" in formular:
            # display the formular and say goodbye.
            print("Die Formel lautet: '[Dollar] ÷ 1.0879 = Euro'. \n")
            print("Vielen Dank für die Aufgabe, auf Wiedersehen!")
        #, else if the input is no:
        elif "N" in formular or "n" in formular:
            # say okay, thank the user for the task and say goodbye.
            print("Okay")
            print("\nVielen Dank für die Aufgabe, auf Wiedersehen!")
        #, else raise an Error telling the user that they have entered an invalid expression.
        else:
            raise SyntaxError("Ungültiger Ausdruck")

    # Else if the user chose no for the confirmation:
    elif "N" in confirmation or "n" in confirmation:
        # ask the user if they still want to know the formular,
        print("\nOkay, möchten Sie trotzdem die Formel wissen?")
        still_formular = inputimeout(prompt = 'J / N   ')
        # if the user still wants to know the formular:
        if "J" in still_formular or "j" in still_formular:
            # display the formular and say goodbye.
            print("Die Formel lautet: '[Dollar] ÷ 1.0879 = Euro'. \n")
            print("Vielen Dank für die Aufgabe, auf Wiedersehen!")
        # else if the user doesn't want to know the formular:
        elif "N" in still_formular or "n" in still_formular:
            print("\n Alles klar, auf Wiedersehen!")
        # else raise an Error telling the user that 
        else:
            raise SyntaxError("Ungültiger Ausdruck.")
        
        
        
        
        
# Else if an invalid language has been added tell the user that the lanugage has not been added yet.
else:
    raise SyntaxError("language not added yet...   |   Sprache noch nicht hinzugefügt...")
