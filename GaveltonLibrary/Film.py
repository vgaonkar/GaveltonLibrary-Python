#Film.py
#Gaonkar, Vijay
#vrgaonkar

from Media import Media


class Film(Media):

    def __init__(self, call_no, title, subject, director, notes, year):
        super(Film, self).__init__(call_no, title, subject, notes)
        self.director = director
        self.year     = year

    def contains_other(self, other):
        return other in self.director or other in self.notes or other in self.year

    def display(self):
        print("\t\t\t ================================== FILM ================================== ")
        super(Film, self).display()
        print(" Director: " + self.director + "\n" +
              " Year: " + self.year + "\n")