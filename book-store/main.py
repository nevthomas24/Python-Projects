def main():
    try:
        # intialize boook list
        booksList = []
        infile = open("theBooksList.txt", "r")
        line = infile.readline()
        while line:
            booksList.append(line.rstrip("\n").split(","))
            line = infile.readline()
        infile.close() 

    except FileNotFoundError:
        print("the <theBooksList.txt> file is not found")
        print("Starting a new books list!")   
        booksList = []    

    choice = 0
    while choice != 4:
        print("*** Books Manager ***")
        print("1) Add a Book")
        print("2) Lookup a Book")
        print("3) Display Books")
        print("4) Quit")
        choice = int(input())

        if choice == 1:
            print("Adding a book...")
            nBook = input("Enter the name of the book:  ")
            nAuthor = input("Enter the name of the Author:  ")
            nPages = input("Enter the number of the pages:  ")
            booksList.append([nBook, nAuthor, nPages])

        elif choice == 2:
            keyword = input("Enter the search term: ")
            if keyword == "":
                print("Please enter a search term: ")
            else:
                print("Looking for a Book.... ")
                for book in booksList:
                    if keyword in book:
                        print(book)

        elif choice == 3:
            print("Displaying All Available Books")
            for i in range(len(booksList)):
                print(booksList[i])

        else:
            print("***QUIT PROGRAM**")

    #saving to external TXT file
    outfile = open("theBooksList.txt", "w")
    for book in booksList:
        outfile.write(",".join(book) + "\n")
    outfile.close()    
    



if __name__ == "__main__":
    main()
