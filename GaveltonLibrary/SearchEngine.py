#SearchEngine.py
#Gaonkar, Vijay
#vrgaonkar

from Book import Book
from Periodical import Periodical
from Film import Film
from Video import Video


class SearchEngine(object):

    card_catalog = []

    def __init__(self):
        book = open("book.txt", "r")
        for line in book:
            data = line.strip().split("|")
            self.card_catalog.append(Book(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9]))
	book.close()

        periodical = open("periodic.txt", "r")
        for line in periodical:
            data = line.strip().split("|")
            self.card_catalog.append(Periodical(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11]))
        periodical.close()

        video = open("video.txt", "r")
        for line in video:
            data = line.strip().split("|")
            self.card_catalog.append(Video(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))
        video.close()

        film = open("film.txt", "r")
        for line in film:
            data = line.strip().split("|")
            self.card_catalog.append(Film(data[0], data[1], data[2], data[3], data[4], data[5]))
        film.close()

    def search_by_call_no(self, search_str):
        result = []
        for item in self.card_catalog:
            if item.contains_call_no(search_str) == True:
		result.append(item)
        return result

    def search_by_title(self, search_str):
        result = []
        for item in self.card_catalog:
            if item.contains_title(search_str) == True:
                result.append(item)
        return result

    def search_by_subject(self, search_str):
        result = []
        for item in self.card_catalog:
            if item.contains_subject(search_str) == True:
                result.append(item)
        return result

    def search_by_other(self, search_str):
        result = []
        for item in self.card_catalog:
            if item.contains_other(search_str) == True:
                result.append(item)
        return result
