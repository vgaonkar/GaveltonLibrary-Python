#Media.py
#Gaonkar, Vijay
#vrgaonkar

from __future__ import print_function


class Media(object):

    def __init__(self, call_no, title, subject, notes):
        self.call_no = call_no
        self.title   = title
        self.subject = subject
        self.notes   = notes

    def contains_title(self, title):
        return title in self.title

    def contains_call_no(self, call_no):
        return call_no in self.call_no

    def contains_subject(self, subject):
        return subject in self.subject

    def display(self):
        print(" Title: " + self.title + "\n" +
              " Call Number: " + self.call_no + "\n" +
              " Subject: " + self.subject + "\n" +
              " Notes: " + self.notes)