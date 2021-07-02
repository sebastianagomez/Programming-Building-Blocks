with open("Week 11/courses.txt") as courseFile:
    for line in courseFile:
        print(line)

# ------------ Strings

colors = "red green blue yellow pink"
                        #","
colorParts = colors.split()

print(colors)
print(colorParts)

for color in colorParts:
    print(color)

# -------------- White Space

name = "   Sebastian Gomez   \n"

# cleanName = name.strip()
name = name.strip()

print(f"----{name}----")
# print(f"---{cleanName}----")

# -------------

with open("Week 11/courses.txt") as courseFile:
    for line in courseFile:
        
        line = line.strip()

        parts = line.split(",")

        name = parts[0]
        grade = float(parts[1])

        bonusGrade = grade + 3

        print(f"{name} - Grade: {grade}, after bonus: {bonusGrade}")