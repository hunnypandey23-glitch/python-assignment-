import csv

patients = []

with open("patients.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        patients.append(row)

print("Patient Records")
print("----------------")

i = 0
while i < len(patients):
    print("Patient ID:", patients[i]["PatientID"])
    print("Name:", patients[i]["Name"])
    print("Age:", patients[i]["Age"])
    print("Disease:", patients[i]["Disease"])
    print()
    i += 1

patient_id = input("Enter Patient ID to search: ")

i = 0
found = False

while i < len(patients):
    if patients[i]["PatientID"] == patient_id:
        print("\nPatient Found")
        print("Patient ID:", patients[i]["PatientID"])
        print("Name:", patients[i]["Name"])
        print("Age:", patients[i]["Age"])
        print("Disease:", patients[i]["Disease"])
        found = True
        break
    i += 1

if not found:
    print("Patient not found")