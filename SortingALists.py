# SORTING A LIST

# Declaring a variable which is storing an empty list.
my_list = []

# Defining a function to sort the list above.


def sorting(expression):

    # Sorting in ascending order:
    if expression == "asc":
        # Sorting
        my_list.sort()
        # Displaying the changed list.
        print(f"Ascending list: {my_list}")

    # Sorting in descending oder:
    elif expression == "desc":
        # Reverse sorting the list.
        my_list.sort(reverse=True)
        # Displaying the list.
        print(f"Descending order: {my_list}")

    # If nothing is in the list:
    else:
        # Printing the unchanged list.
        print("Unchanged order: " + my_list)


sorting(str(input()))
