#Film.py
#Gaonkar, Vijay
#vrgaonkar

from Media import Media


class Video(Media):

    def __init__(self, call_no, title, subject, description, distributor, notes, series, label):
        super(Video, self).__init__(call_no, title, subject, notes)
        self.description = description
        self.distributor = distributor
        self.series      = series
        self.label       = label

    def contains_other(self, other):
        return other in self.description or other in self.notes or other in self.distributor

    def display(self):
        print("\t\t\t ================================== VIDEO ================================== ")
        super(Video, self).display()
        print(" Description: " + self.description + "\n" +
              " Distributor: " + self.distributor + "\n" +
              " Series: " + self.series + "\n" +
              " Label: " + self.label + "\n")