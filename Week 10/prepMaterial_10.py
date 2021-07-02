the_list = [1,21,4]

first = the_list[0] # gets the first item
second = the_list[1] # gets the second item

index = int(input("Which index would you like to get? "))
user_choice = the_list[index] # gets the item at the index the user typed

print(user_choice) 

    # ITERATING THROUGH A LIST USING AN INDEX

books = [10, 5, 151, 56]

number_of_books = len(books)


for i in range(len(books)):
    book = books[i]
    print(book)

    # PRINTING INDEXES

for i in range(len(books)):
    book = books[i]
    print(f"{i}. {book}")

# WORKING WITH PARALLEL LISTS

names = ["Sebastian", "Leonardo", "Nadia", "Carlos"]
numbers = ["15-0000-4554", "15-0000-1233", "15-8415-0000", "15-5852-0050"]

# ...
# Code here that populates the two lists
# ...

for i in range(len(names)):
    name = names[i]
    number = numbers[i]

    # REMOVING ITEMS FROM A LIST

    print(f"{name} - {number}")

names.pop(3)
numbers.pop(3)

print(f"{name} - {number}")




    

    
