# Book Store (Books Manager)

A command-line book manager written in Python. Add books, search them, view your collection, and keep everything saved between sessions.

## Features

- Add a book with its title, author, and page count
- Look up books by a search term
- Display all saved books
- Saves your list to a text file on quit and reloads it on the next run

## Requirements

- Python 3.8 or newer (no external libraries needed)

## How to run

```
python main.py
```

## Menu

```
*** Books Manager ***
1) Add a Book
2) Lookup a Book
3) Display Books
4) Quit
```

Type the number of an option and press Enter. Your books are saved when you choose **4) Quit**.

## How data is stored

Books are saved to `theBooksList.txt` in the folder you run the program from, one book per line in comma-separated format:

```
Dune,Frank Herbert,412
The Hobbit,J.R.R. Tolkien,310
```

If the file doesn't exist, the program starts with an empty list and creates the file on quit.

## What I practiced

- Functions and the `if __name__ == "__main__"` pattern
- Lists of lists, `for` and `while` loops
- User input and menu logic with `if/elif/else`
- Reading and writing files, and handling `FileNotFoundError` with `try/except`

## Planned improvements

- Case-insensitive, partial-match search
- Input validation for menu choices
- Safer file handling with `with open(...)`
- Switch to the `csv` module so commas in titles don't break the save file
