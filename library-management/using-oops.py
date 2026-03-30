class library:
    def __init__(self,lname):
        self.lname=lname
        self.books=[]
        print(f"Welcome to {self.lname} library")
    
    def add_book(self,bname):
        self.bname=bname
        self.books.append(self.bname)
        print(f"{self.bname} added successfully!")
    
    def display_books(self):
        if len(self.books)==0:
            print("No book available in library!")
        else:
            print("Books available in library are: ")
            for b in self.books:
                print(b)
                
    def issue_books(self,bname):
        if bname in self.books:
            self.books.remove(bname)
            print(f"Book {bname} issued successfully!")
        else:
            print("Book not available")
    
    def return_book(self,bname):
        self.books.append(bname)
        print(f"Book {bname} returned successfully!")
        
obj=library("City Library")

obj.add_book("PYTHON")
obj.add_book("DATA SCIENCE")
obj.add_book("AI BASICS")
obj.display_books()
obj.issue_books("PYTHON")
obj.display_books()
obj.return_book("PYTHON")
obj.display_books()

   
    

