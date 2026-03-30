## library management system ##
library={}
def add_book(library):
    book=input("enter book title: ")
    id=input("enter book id: ")
    library[id]={"title":book,"status":"available"}
    print(f"{book} added successfully!")

def remove_book(library,id):
    if id in library:
        book=library[id]["title"]
        library.pop(id)
        print(f"{book} with id {id} removed successfully!")
    else:
        print(f"Book with id {id} not found! ")


def search_book(library,id):
    if id in library:
        book=library[id]["title"]
        status=library[id]["status"]
        print(f" id: {id} |title: {book} |status: {status}")
    else:
        print(f"Book with id {id} is not available in library!")
        
def issue_book(library, id):
    if id in library:
        book=library[id]["title"]
        library[id]["status"]="issued"
        print(f" book {book} issued successfully!")
        return "issued"
    else:
        print(f"Book with id {id} is not available in library!")
        return "not available"
       
def return_book(library,id):
    if id in library:
        book=library[id]["title"]
        library[id]["status"]="available"
        print(f"Book {book} with id {id} is returned successfully!")
    else:
        print(f"{book} with id {id} is not available in library!")

def display_books(library,id):
    if library:
        print("library books: ")
        for id,book in library.items():
            print(f"{id} | {book['title']} | {book['status']}")
    
        
while True:
    print("-----library management system-----")
    print("1. add book")
    print("2. remove book")
    print("3. search book")
    print("4. issue book")
    print("5. return book")
    print("6. display all books")
    print("7. exit")

    choice=int(input("enter choice: "))
    if choice==1:
        add_book(library)
    elif choice==2:
        id=input("enter book id to remove: ")
        remove_book(library,id)
  
    elif choice==3:
        id=input("enter book id to search: ")
        search_book(library,id)
    elif choice==4:
        id=input("enter book id to issue: ")
        issue_book(library,id)
    elif choice==5:
        id=input("enter book id to return: ")
        return_book(library,id)
    elif choice==6:
        display_books(library,id)
    elif choice==7:
        print("Exiting library system...")
        break
    
    
    