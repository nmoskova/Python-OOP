from project.library import Library

from unittest import TestCase, main


class TestLibrary(TestCase):
    def setUp(self) -> None:
        self.name = "Library"
        self.library = Library(self.name)
        self.author = "Author"
        self.title = "Title"
        self.reader = "Reader"

    def test_library_initialisation_with_correct_name(self):
        self.assertEqual(self.name, self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_library_initialisation_with_empty_string_for_name_raises_error(self):
        name = ""
        with self.assertRaises(ValueError) as error:
            Library(name)

        self.assertEqual("Name cannot be empty string!", str(error.exception))

    def test_add_book_with_new_author_who_is_not_in_books_dict(self):
        self.library.add_book(self.author, self.title)
        self.assertEqual([self.title], self.library.books_by_authors[self.author])

    def test_add_book_with_existing_author_non_existing_title(self):
        new_title = "New Title"
        self.library.add_book(self.author, self.title)
        self.library.add_book(self.author, new_title)
        expected_result = [self.title, new_title]
        self.assertEqual(expected_result, self.library.books_by_authors[self.author])

    def test_add_book_with_existing_author_and_existing_title(self):
        self.library.add_book(self.author, self.title)
        self.library.add_book(self.author, self.title)
        expected_result = [self.title]
        self.assertEqual(expected_result, self.library.books_by_authors[self.author])

    def test_add_reader_creates_empty_list_with_new_reader(self):
        self.library.add_reader(self.reader)
        self.assertEqual([], self.library.readers[self.reader])

    def test_add_reader_who_exists_returns_string(self):
        self.library.add_reader(self.reader)
        actual = self.library.add_reader(self.reader)

        self.assertEqual(f"{self.reader} is already registered in the {self.name} library.", actual)

    def test_rent_book_not_registered_reader_returns_string(self):
        actual = self.library.rent_book(self.reader, self.author, self.title)
        self.assertEqual(f"{self.reader} is not registered in the {self.name} Library.", actual)

    def test_rent_book_with_not_registered_author_returns_string(self):
        self.library.add_reader(self.reader)
        actual = self.library.rent_book(self.reader, self.author, self.title)
        self.assertEqual(f"{self.name} Library does not have any {self.author}'s books.", actual)

    def test_rent_book_with_not_existing_book_title(self):
        self.library.add_reader(self.reader)
        self.library.add_book(self.author, self.title)
        new_title = "new_title"
        actual = self.library.rent_book(self.reader, self.author, new_title)
        self.assertEqual(f"""{self.name} Library does not have {self.author}'s "{new_title}".""", actual)

    def test_rent_book_with_existing_reader_author_and_book_title(self):
        self.library.add_reader(self.reader)
        self.library.add_book(self.author, self.title)
        self.library.rent_book(self.reader, self.author, self.title)
        self.assertEqual([{self.author: self.title}], self.library.readers[self.reader])
        self.assertEqual({self.author: []}, self.library.books_by_authors)







if __name__ == '__main__':
    main()
