def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)
    print(f"Book added: [{book_id}] '{title}' by {author} ({year})")
 
 
def borrow_book(catalog, borrowed_books, book_id):
    if book_id not in catalog:
        print(f"Book ID {book_id} does not exist in catalog.")
    elif book_id in borrowed_books:
        print(f"Book ID {book_id} is already borrowed.")
    else:
        borrowed_books.append(book_id)
        title = catalog[book_id][0]
        print(f"Book borrowed: [{book_id}] '{title}'")
 
 
def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Book returned: ID {book_id}")
    else:
        print(f"Book ID {book_id} was not borrowed.")
 
 
def register_member(members, member_id):
    before = len(members)
    members.add(member_id)
    if len(members) == before:
        print(f"Member {member_id} already registered (duplicate ignored).")
    else:
        print(f"Member registered: {member_id}")
 
 
def show_available(catalog, borrowed_books):
    print("\n--- Available Books ---")
    found = False
    for book_id, details in catalog.items():
        if book_id not in borrowed_books:
            title, author, year = details
            print(f"  [{book_id}] '{title}' by {author} ({year})")
            found = True
    if not found:
        print("  No books available.")
    print("-----------------------")
 
 
def main():
    catalog = {}
    borrowed_books = []
    members = set()
 
    
    add_book(catalog, 101, "Python Crash Course", "Eric Matthes", 2019)
    add_book(catalog, 102, "Clean Code", "Robert C. Martin", 2008)
    add_book(catalog, 103, "The Pragmatic Programmer", "Andrew Hunt", 1999)
    add_book(catalog, 104, "Automate the Boring Stuff", "Al Sweigart", 2020)
 
    print()
 
    
    register_member(members, "M001")
    register_member(members, "M002")
    register_member(members, "M003")
    register_member(members, "M001")    
    print()
 
    
    borrow_book(catalog, borrowed_books, 101)
    borrow_book(catalog, borrowed_books, 103)
 
    
    borrow_book(catalog, borrowed_books, 101)
 
    print()
 
    
    return_book(borrowed_books, 101)
 
    
    show_available(catalog, borrowed_books)
 
 
main()
