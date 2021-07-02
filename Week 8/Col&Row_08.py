user = int(input("How many collums and rows do you want in you multiplication table? "))
num = 1

while num != user + 1:
    for c in range(num, (user + 1) * num, num):
        print(f"{c:5}", end = "") 
    print()
    num = num + 1
    