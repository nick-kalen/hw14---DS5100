import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        book_obj = BookLover(name="FooBoo Junior", email="abc@yahoo.com", fav_genre="Wine Recipes")
        
        book_obj.add_book("4Lk *SELTZER* Recipe", 5)
        
        message = "The book was not added successfully!"
        testValue = book_obj.has_book("4Lk *SELTZER* Recipe")
        self.assertTrue(testValue, message)
        
     
    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        book_obj = BookLover(name="FooBoo Junior", email="abc@yahoo.com", fav_genre="Wine Recipes")
        book_obj.add_book("4Lk *SELTZER* Recipe", 5)
        book_obj.add_book("4Lk *SELTZER* Recipe", 5)
        
        message = "There is not 1 instance of the book"
        book_obj.add_book("4Lk *SELTZER* Recipe", 5)
        self.assertEqual(sum(book_obj.book_list.iloc[:,0] == "4Lk *SELTZER* Recipe"), 1, message)
     
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        book_obj = BookLover(name="FooBoo Junior", email="abc@yahoo.com", fav_genre="Wine Recipes")
        book_obj.add_book("4Lk *SELTZER* Recipe", 5)
        value = book_obj.has_book("4Lk *SELTZER* Recipe")
        message = "You do not have the book"
        self.assertTrue(value, message)
     
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        book_obj = BookLover(name="FooBoo Junior", email="abc@yahoo.com", fav_genre="Wine Recipes")
        book_obj.add_book("4Lk *SELTZER* Recipe", 5)
        value = book_obj.has_book("Terrible Wine Recipe")
        message = "Either the book was added incorrectly, or was not checked right."
        self.assertFalse(value, message)
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        book_obj = BookLover(name="FooBoo Junior", email="abc@yahoo.com", fav_genre="Wine Recipes")
        book_obj.add_book("4Lk *SELTZER* Recipe", 5)
        book_obj.add_book("4Lk *CHARDONNAY* Recipe", 5)
        book_obj.add_book("4Lk *ROSE* Recipe", 5)
        value = book_obj.num_books_read()
        message = "The number of books does not match the correct number"
        self.assertEqual(value, 3, message)
     
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        book_obj = BookLover(name="FooBoo Junior", email="abc@yahoo.com", fav_genre="Wine Recipes")
        book_obj.add_book("4Lk *SELTZER* Recipe", 5)
        book_obj.add_book("4Lk *CHARDONNAY* Recipe", 1)
        value = len(book_obj.fav_books())
        message = "The method does not correctly filter books with rating > 3"
        self.assertEqual(value, 1, message)
        
if __name__ == '__main__':

    unittest.main(verbosity=3)