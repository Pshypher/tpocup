# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 02:06:24 2018

@author: Pshypher
"""

# Program reads a list of book and authors in a file and put them in a 
# dictionary. The books are displayed organized by authors

file_pointer = open("book_titles.tsv", 'r')
books_dict = {} # initialize an empty dictionary, maps names of authors to a 
                # collection of books they've written

# read each line of the file
for line_str in file_pointer:
    line_str = line_str.strip()
    if "Work" in line_str:    # skip header
        continue
    book_authors_list = line_str.split('\t')
    book_title_str = book_authors_list[0]  # the title of the book
    if len(book_authors_list) < 2:  # book titles with no author(s)
        books_dict[tuple()] = [book_title_str]
        continue
    author_str = book_authors_list[1] # author(s)
    # 'and' between words in the second field (authors), hint at books written 
    # by more than one author
    authors_list = author_str.split("and")
    # list of tuples containing the first and last names of each author
    for i,name in enumerate(authors_list):
        author_names = tuple(name.split())
        authors_list[i] = author_names
    # the list of authors that co-wrote a book is changed to a tuple
    authors_tuple = tuple(authors_list)        
        
    # add the author(s), book_title pair into the dictionary
    if authors_tuple in books_dict:
        books_dict[authors_tuple].append(book_title_str)
    else:
        books_dict[authors_tuple] = [book_title_str]
            
file_pointer.close()    # close the file

for coauthors in books_dict:
    print("Authors:",end=' ')
    for author in coauthors:
        author_str = ' '.join(author)
        print(author_str, end=' ')
        
    books_written_str = ', '.join(books_dict[coauthors])
    print("\n\tBooks:", books_written_str)