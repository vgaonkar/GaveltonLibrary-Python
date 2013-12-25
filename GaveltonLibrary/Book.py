#Book.py
#Gaonkar, Vijay
#vrgaonkar

from Media import Media


class Book(Media):

    def __init__(self, call_no, title, subject, author, description, publisher, city, year, series, notes):
        super(Book, self).__init__(call_no, title, subject, notes)
        self.author      = author
        self.description = description
        self.publisher   = publisher
        self.city        = city
        self.year        = year
        self.series      = series

    def contains_other(self, other):
        return other in self.description or other in self.notes or other in self.year

    def display(self):
        print("\t\t\t ================================== BOOK ================================== ")
        super(Book, self).display()
        print(" Author: " + self.author + "\n" +
              " Description: " + self.description + "\n" +
              " Publisher: " + self.publisher + "\n" +
              " City: " + self.city + "\n" +
              " Year: " + self.year + "\n" +
	          " Series: " + self.series + "\n")
