people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

for list in people:
        
        item = list.strip()

        parts = list.split(" ")

        name = parts[0]
        age = int(parts[1])

        minAge = min(age)

        # print(f"Name: {name} and Age: {age}")

print(f"The youngest age is {minAge}")