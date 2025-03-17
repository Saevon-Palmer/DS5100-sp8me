import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
        bl = BookLover("Luke Skywalker", "luke@force.com", "sci-fi")
        bl.add_book("Star Wars: Jedi Rising", 5)
        self.assertTrue("Star Wars: Jedi Rising" in bl.book_list['book_name'].values)

    def test_2_add_book(self):
        bl = BookLover("Leia Organa", "leia@resistance.com", "sci-fi")
        bl.add_book("Dune", 5)
        bl.add_book("Dune", 5)
        self.assertEqual(len(bl.book_list[bl.book_list['book_name'] == "Dune"]), 1)

    def test_3_has_read(self):
        bl = BookLover("Yoda", "yoda@jedi.com", "philosophy")
        bl.add_book("The Jedi Path", 4)
        self.assertTrue(bl.has_read("The Jedi Path"))

    def test_4_has_read(self):
        bl = BookLover("Darth Vader", "vader@sith.com", "dark-side")
        self.assertFalse(bl.has_read("Jedi Code"))

    def test_5_num_books_read(self):
        bl = BookLover("Obi-Wan Kenobi", "obiwan@jedi.com", "sci-fi")
        bl.add_book("Master and Apprentice", 4)
        bl.add_book("Kenobi", 5)
        self.assertEqual(bl.num_books_read(), 2)

    def test_6_fav_books(self):
        bl = BookLover("Palpatine", "palpatine@empire.com", "sith")
        bl.add_book("Dark Empire", 5)
        bl.add_book("Sith Revived", 4)
        bl.add_book("The Fall of the Republic", 3)
        favs = bl.fav_books()
        self.assertTrue(all(favs['book_rating'] > 3))

if __name__ == '__main__':
    unittest.main(verbosity=3)