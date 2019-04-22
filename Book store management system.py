'''Book Store Management System'''
from tkinter import *


#Creating Node Class
class Node:
    def __init__(self, bookid, name, cost, author, quantity, bound):
        #initializing node attributes using __init__ constructor
        self.name = name
        self.bookid = bookid
        self.cost = cost
        self.author = author
        self.quantity = quantity
        self.bound = bound
        self.next = None
'''
class User:
    def __init__(self,name, m_no, city, qt, date):
        self.name = name
        self.m_no = m_no
        self.city = city
        self.qt = qt
        self.date = date

    def user_detail(self):
        s=User()
        name = input("Enter User's Name:")
        m_no = input("Enter Mobile No:")
        city = input("Enter City:")
        qt = input("Quantity of book buyed:")
        date = input("Enter book purchased date (DD/MM/YYYY):")
        a=s()
        '''

#Linked List Data Structure creation for various functions in a book store
class Linked_list:

    #defining Head
    def __init__(self):
        self.head = None

    #Function to add book in the linked list
    def add_book(self, bookid, name, cost, author, quantity, bound):

        s = self.head
        newbook = Node(bookid, name,cost,author,quantity,bound)
        if s == None:
            self.head = newbook
        else:
            s = self.head
            while s.next is not None:
                s = s.next
            s.next = newbook

    #Remove book from the linked list
    def remove_book_by_name(self, key):
        c = 1
        curr = self.head
        if curr.name == key:
            self.head = curr.next
        else:
            while curr != None:
                if curr.name == key:
                    prev.next = curr.next
                    return
                #assining values to previous and current values
                prev = curr
                curr = curr.next
                c+=1


    #printing every node in the list
    def print_list(self):
        s = self.head
        while s is not None:
            print ("Book id:",s.bookid,"\tName:" ,s.name,"\tCost:", s.cost,"\tAuthor:",s.author,"\tQuantity:",s.quantity,"\tBound:", s.bound)
            s = s.next

    #searching the book by its name
    def search_by_name(self, key):

        s = self.head
        #declare found inorder to count no of books equal to the searched key
        found = 0
        while s is not None:
            if s.name.lower() == key.lower():
                print("Book found!")
                print ("Book id:",s.bookid,"\tName:" ,s.name,"\tCost:", s.cost,"\tAuthor:",s.author,"\tQuantity:",s.quantity,"\tBound:", s.bound)
                found = 1
                break
            else:
                s = s.next
        if found == 0:
            print("Book not found!")

    #search the book by its id
    def search_by_id(self, key):
        s = self.head
        found = 0
        while s is not None:
            if s.bookid == key:
                print("Book found!")
                print ("Book id:",s.bookid,"\tName:" ,s.name,"\tCost:", s.cost,"\tAuthor:",s.author,"\tQuantity:",s.quantity,"\tBound:", s.bound)
                found = 1
                break
            else:
                s = s.next
        if found == 0:
            print("Book not found!")

    #search book by the author's name
    def search_by_author(self,key):
        s = self.head
        found = 0
        while s is not None:
            if s.author == key:
                print("Book found!")
                print ("Book id:",s.bookid,"\tName:" ,s.name,"\tCost:", s.cost,"\tAuthor:",s.author,"\tQuantity:",s.quantity,"\tBound:", s.bound)
                s = s.next
                found+=1
            else:
                s = s.next
        if found == 0:
             print("Book not found!")


    #function to update a book's purchase from the store by storing all the purchased books in the buyed_book array and updating the book node
    def buy_book(self):

        #user detail array to store the customer's puchase
        user_detail=[]

        #array to show the book's being sold
        buyed_book = []

        #details of the customer and the book he/she purchased
        name = input("Enter User's Name:")
        m_no = input("Enter Mobile No:")
        city = input("Enter City:")
        qt = int(input("Quantity of books buyed:"))
        buy_date = input("Enter book purchased date (DD/MM/YYYY):")
        book_id = input("Enter the book id:")

        #object instance of user detail inorder to append it in the list
        ud = str(book_id) +"\t" + str(name) + "\t" + str(m_no) + "\t" + str(city) + "\t" + str(qt) + "\t" + str(buy_date)
        user_detail.append(ud)

        #loop till the no of specified books qt is reached
        while qt!= 0:
            print ("Search purchased book by:\n1) Id\n2) Name")
            choice = int(input("Select Option:"))
            if choice == 1:

                #buy book by its id
                key = int(input("Enter book Id:"))
                s = self.head
                found = 0
                while s is not None:
                    if s.bookid == key:
                        st=str( str(s.bookid)) + "\t"+str(s.name)+"\t"+str(s.cost) +"\t"+str(s.author)+"\t"+str(int(s.quantity) -1)+"\t"+str(s.bound)
                        s.quantity = int(s.quantity) - 1
                        buyed_book.append(st)
                        found = 1
                        break
                    else:
                        s = s.next
                if found == 0:
                    print("Book not found!")
                if found>0:
                    print("Hey!! Thanks for Purchasing!")

                for string in buyed_book:
                    print(string)
                for st in user_detail:
                    print(st)
                    #for s in string:
                        #print ("Book id:",s.bookid,"\tName:" ,s.name,"\tCost:", s.cost,"\tAuthor:",s.author,"\tQuantity:",s.quantity,"\tBound:", s.bound)

            #buy book by its name
            elif choice==2:
                key = input("Enter book Name:")
                s = self.head
                found = 0
                while s is not None:
                    if s.name.lower() == key.lower():
                        st=str(s.bookid) + "\t"+str(s.name)+"\t"+str(s.cost) +"\t"+str(s.author)+"\t"+str(int(s.quantity) -1)+"\t"+str(s.bound)
                        borrowed_book.append(st)
                        found = 1
                        break
                    else:
                        s = s.next
                if found == 0:
                    print("Book not found!")
                for string in borrowed_book:
                    print("Book id")
                    print("HEyyy!! your borrow book")
                    print(string)
            else:
                print("You enter invalid choice")
            qt = qt - 1

            def buyedbooks(self):
                for i in buyed_book:
                    print (i)

    '''def userdetails(self):
            for i in Linked_list.buy_book.u
                print(i)
    '''

    #update a book's details
    def update_book(self):
        key = int(input("Enter Book Id you want to Update:"))
        s = self.head
        found = 0

        #search the book in list
        while s is not None:
            if s.bookid == key:
                print("Book found!")
                print ("Book id:",s.bookid,"\tName:" ,s.name,"\tCost:", s.cost,"\tAuthor:",s.author,"\tQuantity:",s.quantity,"\tBound:", s.bound)
                found += 1

                #different options for updating the data
                print("What do you want to update?\n1) Id\n2) Name\n3) Cost \n4) Author\n5) Quantity\n6) Bound")
                choice = int(input("Enter your Choice:"))
                if choice==1:
                    new_id = int(input("Enter the Id:"))
                    s.bookid = new_id

                elif choice==2:
                    new_name = input("Enter New Name:")
                    s.name = new_name

                elif choice == 3:
                    new_cost = input("Enter New Cost:")
                    s.cost = new_cost

                elif choice == 4:
                    new_author = input("Enter New Author Name:")
                    s.author = new_author

                elif choice == 5:
                    new_quantity = int(input("Enter the New Quantity:"))
                    s.quantity = new_quantity

                elif choice == 6:
                    new_bound = input("Enter New Bound:")
                    s.bound = new_bound

                #elif choice == 7:
                #       exit()
            else:
                s = s.next

        if found == 0:
            print("Book not found!")




        '''elif choice == 2:
            key = str(input("Enter book Name:"))
            Linked_list.search_by_name(key)'''






def main():
    master = Tk()
    l = Linked_list()
    while True:
        print("Choose an option:\n1) Add Book\n2) Remove book\n3) Buy Book\n4) Update Book\n5) Display\n6) Search Book\n7) Exit")
        ch=IntVar()
        Label(master, text="Enter your choice").grid(row=0)
        entry_box=Entry(master,textvariable=ch)
        entry_box1=Entry(master,textvariable=ch)
        entry_box.grid(row=0, column=1)
        def action():
            final=ch.get()
            print(final)
        #choice = int(input("Enetr the option number:"))
            if final== 1:
                id=IntVar()
                name=StringVar()
                price=StringVar()
                aut=StringVar()
                amt=IntVar()
                bound=StringVar()
                Label(master, text="Book id").grid(row=2)
                Label(master, text="Book Name").grid(row=3)
                Label(master, text="Price").grid(row=4)
                Label(master, text="Auther Name").grid(row=5)
                Label(master, text="Book Quantity").grid(row=6)
                Label(master, text="Bound").grid(row=7)
                Entry(master,textvariable=id).grid(row=2, column=1)
                Entry(master,textvariable=name).grid(row=3, column=1)
                Entry(master,textvariable=price).grid(row=4, column=1)
                Entry(master,textvariable=aut).grid(row=5, column=1)
                Entry(master,textvariable=amt).grid(row=6, column=1)
                Entry(master,textvariable=bound).grid(row=7, column=1)
                def action2():
                    id1=id.get()
                    name1=name.get()
                    price1=price.get()
                    aut1=aut.get()
                    amt1=amt.get()
                    bound1=bound.get()
                    l.add_book(id1, name1, price1, aut1, amt1, bound1)
                    print("data Successfully added!!!")

                Button(master,text="submit",command=action2).grid(row=7,column=5)

            elif final == 2:
                key = input("Enter the book name you want to remove:")
                l.remove_book_by_name(key)
                print("your book successfully remove")
            elif final == 3:
                l.buy_book()
            elif final == 4:
                l.update_book()
            elif final == 5:
                l.print_list()
            elif final == 6:
                print("Search book by:\n1) Book Id\n2) Name\n3) Author")
                ch1=IntVar()
                Label(master, text="Enter your choice for searching").grid(row=1)
                Entry(master,textvariable=ch1).grid(row=1, column=1)
                def action1():
                    final1=ch1.get()
                    if final1 == 1:
                        key = int(input("Enter the book id you want to search:"))
                        l.search_by_id(key)
                    elif final1 == 2:
                        key = input("Enter the book name you want to search:")
                        l.search_by_name(key)
                    elif final1 == 3:
                        key = input("Enter thse author's name you want to search:")
                        l.search_by_author(key)
                    else:
                        print("invalid choice for searching")
                btt1=Button(master,text="submit",command=action1)
                btt1.grid(row=1,column=2)
            elif final == 7:
                l.buy_book()
            elif final == 8:
                pass
            else:
                print("Invalid choice")

        btt=Button(master,text="submit",command=action)
        btt.grid(row=0,column=2)
            #choice = int(input("Enetr the option number:"))
        mainloop( )




if __name__ == "__main__":
    main()
