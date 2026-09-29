file = open("students.txt", "r")

data = file.read()

print(data)

file.close()

with open("students.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()

    print(line1)
    print(line2)

output = open("output.txt", "w")

output.write(line1)
output.write(line2)

output.close()