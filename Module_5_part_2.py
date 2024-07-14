def main():
    # Prompt the user to enter the number of books purchased
    num_books = int(input("Enter the number of books purchased this month: "))
    
    # Calculate points based on the number of books
    if num_books == 0:
        points = 0
    elif num_books == 2:
        points = 5
    elif num_books == 4:
        points = 15
    elif num_books == 6:
        points = 30
    elif num_books >= 8:
        points = 60
    else:
        points = 0  # Default case if number of books is negative or between 1 and 7
    
    # Display the points awarded
    print(f"Points awarded: {points}")

# Call the main function to run the program
main()
