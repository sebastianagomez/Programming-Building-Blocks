largest_numbers = 0
largest_book = ""
mormon = "Book of Mormon"

with open("books_and_chapters.txt") as sacredList:

    for line in sacredList:
        line = line.strip()
        parts = line.split(":")
        Scripture = parts[2]
        Book = parts[0]
        Chapters = parts[1]
        
    #     hola = int(Chapters)
    #     if hola > largest_numbers:
    #         largest_numbers = hola
    #         largest_book = Book
    # print(largest_numbers)
    # print(largest_book)
        if mormon == Scripture:
            print(f"{Book} {Chapters}")