print("Please enter the following information:")

print()

first_name = input("First Name: ")
last_name = input("Last Name: ")
email = input("Email Address: ")
phone = input("Phone Number: ")
job_title = input("Job Title: ")
id_number = input("ID Number: ")

print("The ID Card is:")

print("-----------------------")

print(last_name.upper() + ", " + first_name)
print(job_title.title())
print("ID: " + id_number)

print()

print(email.lower())
print(phone)