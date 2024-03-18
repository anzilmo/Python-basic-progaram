basicsalary = int(input("Enter basic salary: "))

if basicsalary <= 10000:
    HRA = basicsalary * 0.20
    DA = basicsalary * 0.80
elif basicsalary <= 20000:
    HRA = basicsalary * 0.25
    DA = basicsalary * 0.90
else:
    HRA = basicsalary * 0.30
    DA = basicsalary * 0.95

Grosssalary = basicsalary + HRA + DA
print("Gross salary is:", Grosssalary)
