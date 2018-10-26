# Exercise 1: Work with the person next to you to design classes to manage
# the products, customers, and purchase orders for an online book store
# such as amazon.com. Outline the data attributes and useful methods 
# for each class. You can discuss and create the outline together. 

import time
import random 
import string

available_books = {} 
customers = {} 
purchases = {} 


class Book(object): 
    '''Book class for the products. Will hold info on title, author, price and unique ID'''
    
    next_id_num = 1 # Class variable to keep track of products. 
    
    def __init__(self, title, author, price):
        '''Creates Book using title, author, price. Assings ID'''
        
        if len(available_books.keys()) == 0:
            self.title = title
            self.author = author
            self.price = price
            self.id_num = Book.next_id_num # Assign ID. 
            Book.next_id_num += 1 # Increase ID by 1 for next Book
        
        else:
            for id_num in available_books.keys(): # Run through all Book IDs
                if available_books[id_num][0] == title and available_books[id_num][1] == author:
                    ans = str(input("Book is already in memory. Do you want to update the price? Y/N ")).lower()
                    if ans == 'y':
                        new_p = float(input("Please write down the new price: "))
                        available_books[id_num][2] = new_p
                else:
                    self.title = title
                    self.author = author
                    self.price = price
                    self.id_num = Book.next_id_num # Assign ID. 
                    Book.next_id_num += 1 # Increase ID by 1 for next Book
        
        if self.title == title:
            available_books[self.id_num] = [self.title, self.author, self.price] # Update dictionary        

            
    def get_title(self):
        '''Gets selfs title'''
        return self.title
    
    def get_author(self):
        '''Gets selfs author name'''
        name = self.author.split()
        if len(name) >= 2:
            return name[1] + ', ' + name[0]
        else:
            return self.author
    
    def update_price(self, new_price):
        '''Allows to update price'''
        if type(new_price) in (int, float):
            self.price = new_price
            available_books[self.id_num][2] = new_price
        else:
            print("That is not a valid price.")

    def book_id(self):
        return self.id_num
        
    def __str__(self):
        '''Returns info on book'''
        return 'The book ' + self.title + ' by ' + self.author + \
    ' has the ID number ' + str(self.id_num) + ' and a price of ' + str(self.price)
    
    def __lt__(self, other):
        '''Orders by id num'''
        return self.id_num < other.id_num


# Class for customers

class Customer(object):
    '''Customer class, gives a random unused ID'''
    
    def __init__(self, name, email):
        '''Creates Customer profile'''
        email_check = str(email).lower()
        if '@' not in email_check:
            print("This is not a valid email. Try again.")
        for cust_id in customers:
            if customers[cust_id][1] == email_check:
                print("That email is already in use.")
            else:
                self.email = email
                self.name = str(name)
                new_id = random.randint(1,10000) # Random int from 1 to 10K
                while new_id in customers:
                    new_id = random.randint(1,10000)
                self.cust_id = new_id # Assign ID
                customers[self.cust_id] = [self.name, self.email]
        
    def get_name(self):
        '''Returns customer name'''
        return self.name
    
    def get_email(self):
        '''Returns customer email'''
        return self.email
    
    def cust_id(self):
        '''Returns customer id'''
        return self.cust_id
    
    def __str__(self):
        '''Prints info'''
        return 'Customer ' + str(self.cust_id) + ' is called ' + self.name + ' and has email ' + self.email
    

# Purchase
class Purchase(Book, Customer):

    # Create a random alphanumeric purchase ID
    
    def __init__(self, id_book, id_cust):
        '''Creates a purchase instance with the id of book and cust'''
        if id_book not in available_books:
            print("The book is not available for purchase.")
            pass
        elif id_cust not in customers:
            print("Unrecognized customer.")
            pass
        else:
            purchase_id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))
            while purchase_id in purchases:
                purchase_id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16)) 
            self.purchase_id = purchase_id
            self.day = time.strftime("%d/%m/%Y")
            self.time = time.strftime("%H:%M:%S")
            customers[self.purchase_id] = [id_book, id_cust, self.day, self.time]

    def get_day(self):
        '''Day of purchase'''
        return self.day
    
    def get_time(self):
        '''Time of purchase'''
        return self.time
    
    def __str__(self):
        return 'Purchase number ' + str(self.purchase_id) 
    
        
b1 = Book('El Coleccionista de Flechas', 'Cristian Perfumo', 3.99) # New valid entry
print(b1)

b2 = Book('Harry Potter 1', 'JK Rowling', 9.99) # New valid entry
print(b2)

#b3 = Book('Harry Potter 2', 'JK Rowling') # Testing new entry with existing author
#b3.set_price(9.99)
#b4 = Book('El Coleccionista de Flechas', 'Cristian Perfumo') # Existing entry to test 

#c1 = Customer('Alvaro', 'alvaroaguirre@outlook.com')
#c2 = Customer('Enrique', 'a.e.aguirre-moya@lse.ac.uk')
#c3 = Customer('Carlos', 'alvaroaguirre@outlook.com')

print(available_books)
#print(customers)
#print(purchases)