with open("Week 11/books.txt") as bookFile:

    for line in bookFile:
        
        book = line.strip()

        print(book)

line = "     text"

line.strip(" ")

print(line)