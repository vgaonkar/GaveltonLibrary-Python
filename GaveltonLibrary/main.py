#main.py
#Gaonkar, Vijay
#vrgaonkar

from __future__ import print_function
from SearchEngine import SearchEngine

search_engine = SearchEngine()
results = []
choice = 0

while choice != 5:
    print("\n\t\t\t ###############################  GAVELTON LIBRARY ############################### \n"
          "\n Welcome! Looking for something? I can help!")

    search_str = raw_input("\n Enter a word or a phrase to get started: ")
    print("\n How do you wanna search?\n"
          " 1. Search by call number\n"
          " 2. Search by title\n"
          " 3. Search by subject\n"
          " 4. Search by other\n"
          " 5. Quit\n")
    choice = input(" Your Choice: ")

    if choice == 1:
        results = search_engine.search_by_call_no(search_str)
        if len(results) > 0:
            print("\n\t\t\t ************************** Search Results ************************** ")
            for item in results:
		item.display()

        else:
            print("\n Sorry no results found with <" + search_str + "> in call number")

    elif choice == 2:
        results = search_engine.search_by_title(search_str)
        if len(results) > 0:
            print("\t\t\t ************************** Search Results ************************** ")
            for item in results:
                item.display()

        else:
            print("\n Sorry no results found with <" + search_str + "> in title")

    elif choice == 3:
        results = search_engine.search_by_subject(search_str)
        if len(results) > 0:
            print("\t\t\t ************************** Search Results ************************** ")
            for item in results:
                item.display()

        else:
            print("\n Sorry no results found with <" + search_str + "> in subject")

    elif choice == 4:
        results = search_engine.search_by_other(search_str)
        if len(results) > 0:
            print("\t\t\t ************************** Search Results ************************** ")
            for item in results:
                item.display()

        else:
            print("\n Sorry no results found with <" + search_str + ">")

    elif choice == 5:
        exit()

    else:
        print("\n How do you wanna search?\n" +
          " 1. Search by call number\n" +
          " 2. Search by title\n" +
          " 3. Search by subject\n" +
          " 4. Search by other\n" +
          " 5. Quit\n")
        choice = input(" Your Choice: ")

    print("\n Found what you were looking for?\n" +
          " 1. Yes, done searching\n" +
          " 2. No, start a new search\n")
    end_choice = input(" Your Choice: ")

    while end_choice != 3:

        if end_choice == 1:
            exit()

        elif end_choice == 2:
            break

        else:
            print("\n Found what you were looking for?\n" +
              " 1. Yes, done searching\n" +
              " 2. No, start a new search\n")
            end_choice = input(" Your Choice: ")
