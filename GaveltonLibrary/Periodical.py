#Periodical.py
#Gaonkar, Vijay
#vrgaonkar

from Media import Media


class Periodical(Media):

    def __init__(self, call_no, title, subject, author, description, publisher, publishing_history, series, notes, related_titles, other_forms_of_title, govt_doc_no):
        super(Periodical, self).__init__(call_no, title, subject, notes)
        self.author               = author
        self.description          = description
        self.publisher            = publisher
        self.publishing_history   = publishing_history
        self.series               = series
        self.related_titles       = related_titles
        self.other_forms_of_title = other_forms_of_title
        self.govt_doc_no          = govt_doc_no

    def contains_other(self, other):
        return other in self.description or other in self.notes or other in self.series or other in self.related_titles

    def display(self):
        print("\t\t\t =============================== PERIODICAL =============================== ")
        super(Periodical, self).display()
        print(" Author: " + self.author + "\n" +
              " Description: " + self.description + "\n" +
              " Publisher: " + self.publisher + "\n" +
              " Publishing History: " + self.publishing_history + "\n" +
              " Series: " + self.series + "\n" +
              " Related Titles: " + self.related_titles + "\n" +
              " Other Forms of Title: " + self.other_forms_of_title + "\n" +
              " Govt. Doc. Number: " + self.govt_doc_no + "\n")