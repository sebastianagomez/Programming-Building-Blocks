with open("Week 11/hr_system.txt") as systemFile:
    for line in systemFile:
        
        line = line.strip()

        parts = line.split(" ")

        name = parts[0]
        idNumber = parts[1]
        jobTitle = parts[2]
        salary = (float(parts[3]) / 2) + 1000


        print(f"{name} (ID: {idNumber}), {jobTitle} - ${salary:.2f}")