import pandas as pd
import numpy as np

class BookLover():
    def __init__(self, name, email, fav_genre, num_books=None, book_list=None):
        self.num_books = 0
        self.book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
        
        
    def add_book(self, book_name, rating):
        if not(self.has_book(book_name)):
            new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [rating]
            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            
            
    def has_book(self, book_name):
        if (book_name in self.book_list.iloc[:,0].values):
            return True
        else:
            return False
        
        
    def num_books_read(self):
        return len(self.book_list)
    
    def fav_books(self):
        books = self.book_list
        return books[books['book_rating'] > 3]