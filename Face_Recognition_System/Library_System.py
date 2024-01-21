# Create the database of books
db = [
    {"Title": "Moby Dick", "Author": "Herman Melville", "Release Date": 1851},
    {"Title": "A Study in Scarlet", "Author": "Sir Arthur Conan Doyle", "Release Date": 1887},
    {"Title": "Frankenstein", "Author": "Mary Shelley", "Release Date": 1818},
    {"Title": "Hitchhikers Guide to the Galaxy", "Author": "Douglas Adams", "Release Date": 1879}
]

# Function to search for a book by title
def search_book(title, database):
    for book in database:
        if book["Title"] == title:
            return book
    return None

###########################################
book_title = "Frankenstein"
result = search_book(book_title, db)

if result:
    print("Book details:")
    print(f"Title: {result['Title']}")
    print(f"Author: {result['Author']}")
    print(f"Release Date: {result['Release Date']}")
else:
    print(f"Book '{book_title}' not found in the database.")
